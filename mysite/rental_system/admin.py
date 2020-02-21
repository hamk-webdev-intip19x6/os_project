from django.contrib import admin

# Register your models here.
from .models import Creator, Type, Work, Genre, Publisher, RentedWork
admin.site.register(Creator)
admin.site.register(Type)
admin.site.register(Work)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(RentedWork)