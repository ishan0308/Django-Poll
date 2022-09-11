from django.shortcuts import render
from poll.models import apollModel, upollModel, tpollModel
from poll.forms import upollForm,tpollForm
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    form = upollForm(request.POST)
    if form.is_valid():
        #ques = request.session['ques']
        ques = apollModel.objects.all()[0]
        p = form.save(commit=False)
        mod = upollModel.objects.all().filter(question=ques,choice=form.cleaned_data['choice'])
        if(len(mod)==0):
            p.question = ques
            p.choice = form.cleaned_data['choice']
            p.vote = 1
            p.save()
        else:
            mod[0].vote +=1
            mod[0].save()
        return HttpResponseRedirect('/poll/addpoll')
    else:
        ques1 = apollModel.objects.all()
        ques = ques1[0].question
        #upollModel.objects.create(question=ques)
        request.session['ques'] = ques
        return render(request,'index.html',{'ques':ques})

def addpoll(request):
    polls = upollModel.objects.all().order_by('question').values()
    return render(request,'index2.html',{'polls':polls})

def tpoll(request):
    form = tpollForm(request.POST or None)
    if form.is_valid():
        ques = form.cleaned_data['question']
        ques1 = ques.question
        p = form.save(commit=False)
        mod = upollModel.objects.all().filter(question=ques,choice=form.cleaned_data['choice'])
        if(len(mod)==0):
            t = upollForm(None)
            q = t.save(commit=False)
            q.question = ques
            q.choice = form.cleaned_data['choice']
            q.vote = 1
            q.save()
        else:
            mod[0].vote += 1
            mod[0].save()
        return HttpResponseRedirect('/poll/addpoll')
    else:
        return render(request,'index3.html',{'form':form})
