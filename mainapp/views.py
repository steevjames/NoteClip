from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def test(request):
    return render(request, 'home.html', {})

def notes(request):
    return render(request, 'notes.html', {})

def del_user(request, username):    
    try:
        # u = User.objects.get(username = username)
        # u.delete()
        if request.user.username==username:
            u = User.objects.get(username = username)
            u.delete()
            return HttpResponse("response");           

    except User.DoesNotExist:
        return render(request, "User doesnot exist")    

    except Exception as e: 
        return render(request, "expception")

    return render(request, 'front.html') 