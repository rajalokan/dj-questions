from django.forms import ModelForm
from django import forms

from .models import Question

class PollForm(forms.Form):
    input = forms.CharField(widget=forms.Textarea)
    # class Meta:
    #     model = Question
    #     fields = ['input']
    #      # 'answer_a', 'answer_b', 'answer_c', 'marks', 'correct_answer']
