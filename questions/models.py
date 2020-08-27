from django.db import models
from django import forms

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer_a = models.CharField(max_length=100)
    answer_b = models.CharField(max_length=100)
    answer_c = models.CharField(max_length=100)
    marks = models.IntegerField()
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question

