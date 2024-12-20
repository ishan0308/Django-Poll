from django import forms
from . import models

class upollForm(forms.ModelForm):
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