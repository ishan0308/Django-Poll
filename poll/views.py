from django.shortcuts import render
from poll.models import apollModel, upollModel, tpollModel
from poll.forms import upollForm,tpollForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Sum
from django.utils.timezone import now
# Create your views here.

def index(request):
    if request.method == "POST":
        # Fetch all questions from `apollModel`
        questions = apollModel.objects.all()

        for ques in questions:
            # Get the user's choice for each question
            choice = request.POST.get(f"choice_{ques.question}")
            if choice:
                # Increment vote count in `upollModel`
                vote_entry = upollModel.objects.filter(question=ques, choice=choice).first()
                if vote_entry:
                    vote_entry.vote += 1
                    vote_entry.save()
                else:
                    # Handle cases where `choice` does not exist in `upollModel`
                    upollModel.objects.create(question=ques, choice=choice, vote=1)

        # Redirect to results page
        return HttpResponseRedirect('/poll/addpoll')
    else:
        # Fetch all questions for display
        questions = apollModel.objects.all()
        return render(request, 'index.html', {'questions': questions})


def addpoll(request):

    # Fetch all questions and aggregate votes for each choice under each question
    results = []
    questions = apollModel.objects.all()

    for question in questions:
        # Get votes for each choice
        choices = upollModel.objects.filter(question=question).values('choice').annotate(total_votes=Sum('vote'))

        # Convert choices to a dictionary for easy lookup
        choice_dict = {choice['choice']: choice['total_votes'] for choice in choices}

        # Ensure both "good" and "bad" are present with default 0 votes
        results.append({
            'question': question.question,
            'choices': [
                {'choice': 'good', 'total_votes': choice_dict.get('good', 0)},
                {'choice': 'bad', 'total_votes': choice_dict.get('bad', 0)},
            ]
        })

    return render(request, 'index2.html', {'results': results})


def tpoll(request):
    form = tpollForm(request.POST or None)
    if form.is_valid():
        ques = form.cleaned_data['question']
        # Create a new question in `apollModel`
        question = apollModel.objects.create(question=ques, timestamp=now())

        # Add default choices in `tpollModel` with vote count as 0
        tpollModel.objects.create(question=question, choice="good", vote=0)
        tpollModel.objects.create(question=question, choice="bad", vote=0)

        return HttpResponseRedirect('/poll/addpoll')  # Redirect to results page
    else:
        return render(request, 'index3.html', {'form': form})
