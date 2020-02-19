from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Work, Type

def index(request):
    works = Work.objects.all()
    types = Type.objects.all()
    context = {'works': works, 'types': types}
    return render(request, 'rental_system/index.html', context)

def work(request, work_id):
    work = Work.objects.get(pk=work_id)
    return render(request, 'rental_system/work.html', {'work': work})