from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    context = {
        'questions': [
            {
                'id': 1,
                'content':
                'Why is there a light in the fridge and not in the freezer?'
            },
            {
                'id': 2,
                'content': 'Why don\'t sheep shrink when it rains?'
            },
            {
                'id': 3,
                'content':
                'Why are the called apartments when they are all together?'
            },
            {
                'id': 4,
                'content':
                    'Why are cigarettes sold where smoking is prohibited?'
            },
        ]
    }
    return render(request, 'quiz/index.html', context)
