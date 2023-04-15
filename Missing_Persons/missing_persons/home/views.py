from django.shortcuts import render
from django.http import HttpResponse
from .models import MissingPersons

# Create your views here.

def indexPageView(request):
    return render(request, 'homepages/index.html')


def aboutView(request):
    return render(request, 'about.html')


def contView(request):
    db_missingPersons = MissingPersons.objects.all()

    context = {
        "data": db_missingPersons
    }
    return render(request, 'missingPersons.html', context)


def personView(request, id):

    db_missingPersons = MissingPersons.objects.get(id=id)

    idDict = {
        'data': db_missingPersons
    }

    return render(request, 'person.html', idDict)
