from django.contrib import admin

# Register your models here.

from mainapp.models import Note

admin.site.register(Note)