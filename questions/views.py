import re

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import PollForm
from .models import Question

def index_view(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            data = form.data['input']
            m = re.findall("(\[([\w\s]+)::([\w\d\s/::]+)\])", data)
            answers = m[1][2].split('/')
            question = Question(
                question=m[0][2],
                answer_a=answers[0].split(':')[1],
                answer_b=answers[1].split(':')[1],
                answer_c=answers[2].split(':')[1],
                marks=int(m[2][2]),
                correct_answer=m[3][2],
            )
            question.save()
            return HttpResponseRedirect("/questions")
    else:
        form = PollForm()
    return render(request, 'index.html', {
        'form': form
    })

def questions_view(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {
        'questions': questions
    })
