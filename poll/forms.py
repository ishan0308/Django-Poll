from django import forms
from . import models

class upollForm(forms.ModelForm):
    #choice = models.ChoiceField(widget=forms.Select,choices=(('easy','easy'),('tough','tough')),default='easy')
    class Meta:
        model = models.upollModel
        exclude=('question','vote')

class apollForm(forms.ModelForm):
    class Meta:
        model = models.apollModel
        exclude = ()

class tpollForm(forms.ModelForm):
    class Meta:
        model = models.tpollModel
        exclude = ('vote',)