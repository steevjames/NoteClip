from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import os

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'home.html', {})

def notes(request):
    return render(request, 'notes.html', {})

def deleteuser(request):    
    try:
        if request.user.username==request.GET['uname']:
            u = User.objects.get(username = request.user.username)
            u.delete()
            return HttpResponse("User Has Been Deleted")         
        else: 
            return HttpResponseRedirect("..") 
    except : 
        return HttpResponse("An Error Occured !")

def deleteaccount(request):
    return render(request, 'deleteaccount.html', {})