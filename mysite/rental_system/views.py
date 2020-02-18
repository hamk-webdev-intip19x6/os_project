from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Work

def index(request):
    works = Work.objects.all()
    context = {'works': works}
    return render(request, 'rental_system/index.html', context)