from django.db import models
from .forms import NameForm

# Create your models here.


class Note(models.Model):
    owner = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=3000)