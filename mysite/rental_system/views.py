from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Work, Type, RentedWork

def index(request):
    works = Work.objects.all()
    types = Type.objects.all()
    context = {'works': works, 'types': types}
    return render(request, 'rental_system/index.html', context)

def work(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    rented = RentedWork.objects.filter(rented_work = work_id);
    return render(request, 'rental_system/work.html', {'work': work, 'rented': rented})

def rented(request):
    current_user = request.user
    rented = list(RentedWork.objects.filter(user_id = current_user.id))
    
    return render(request, 'rental_system/rented.html', {'rented': rented})