from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import os

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def test(request):
    return render(request, 'home.html', {})

def notes(request):
    return render(request, 'notes.html', {})

def deleteuser(request, username):    
    try:
        if request.user.username==username:
            u = User.objects.get(username = username)
            u.delete()
            return HttpResponse("User Has Been Deleted")         
        else: 
            try:
                HOSTNAME = socket.gethostname()
            except:
                HOSTNAME = 'localhost'
            return HttpResponseRedirect("..") 
    except : 
        return HttpResponse("An Error Occured !")