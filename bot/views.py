from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    return render(request, "bot/home.html")


def sobre(request):

    return HttpResponse('SOBRE')


def contato(request):

    return HttpResponse('CONTATO')

# Create your views here.
