from django.contrib import admin

# Register your models here.
from .models import Creator, Type, Work, Genre
admin.site.register(Creator)
admin.site.register(Type)
admin.site.register(Work)
admin.site.register(Genre)