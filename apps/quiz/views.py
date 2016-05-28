from django.shortcuts import render
from apps.quiz.models import User


def index(request):
    context = {}
    return render(request, 'interests/index.html', context)


def interests(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'interests/interests-index.html', context)


def show(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user
    }
    return render(request, 'interests/interests-show.html', context)


# def show(request, question_id):
    # req_question = Question.objects.get(id=question_id)
    # choices = Choice.objects.all().filter(question=req_question)
    # context = {
        # 'question': req_question,
        # 'choices': choices,
    # }
    # return render(request, 'quiz/show.html', context)
