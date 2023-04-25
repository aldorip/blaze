from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    return render(request, "bot/home.html")


def sobre(request):

    return render(request, "bot/sobre.html")


def contato(request):

    return render(request, "bot/contato.html")

# Create your views here.
