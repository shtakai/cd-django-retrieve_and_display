from django.http import HttpResponse, Http404
from django.shortcuts import render


def index(request):
    return render(request, 'quiz/index.html')


def show(request, question_id):
    return HttpResponse(
        "You are looking at question number {}.".format(question_id))
