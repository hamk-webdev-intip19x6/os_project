from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Work

def index(request):
    works = Work.objects.all()
    context = {'works': works}
    return render(request, 'rental_system/index.html', context)

def works(request, work_id):
    work = Work.objects.get(pk=work_id)
    return render(request, 'rental_system/work.html', {'work': work})