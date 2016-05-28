from django.http import HttpResponse, Http404
from django.shortcuts import render
from apps.quiz.models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'quiz/index.html', context)


def show(request, question_id):
    req_question = Question.objects.get(id=question_id)
    choices = Choice.objects.all().filter(question=req_question)
    context = {
        'question': req_question,
        'choices': choices,
    }
    return render(request, 'quiz/show.html', context)
