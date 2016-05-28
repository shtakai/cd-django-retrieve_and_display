from django.http import HttpResponse, Http404
from django.shortcuts import render


def index(request):
    return render(request, 'quiz/index.html')


def show(request, question_id):
    if int(question_id) == 1:
        return HttpResponse(
            "You are looking at question number {}.".format(question_id))
    else:
        raise Http404
