from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def test(request):
    return render(request, 'home.html', {})

def notes(request):
    return render(request, 'notes.html', {})