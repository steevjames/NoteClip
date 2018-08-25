from django.db import models

# Create your models here.


class post(models.Model):
    owner = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=3000)