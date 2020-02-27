from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from operator import attrgetter
from .models import Work, Type, Genre, RentedWork
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    works = Work.objects.all()
    types = Type.objects.all()
    genres = Genre.objects.all()
    context = {'works': works, 'types': types, 'genres': genres}

    #search
    query = ""
    if request.GET:
        query = request.GET['search']
        context['query'] = str(query)
    
    posts = sorted(search(query), key=attrgetter('title'), reverse=True)
    context['posts'] = posts
    

    return render(request, 'rental_system/index.html', context)

def work(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    creators = work.creators.all()
    other_works = list(Work.objects.filter(~Q(id = work_id),creators__in=creators))[:5]
    rented = RentedWork.objects.filter(rented_work_id = work_id)

    return render(request, 'rental_system/work.html', {'work': work, 'rented': rented, 'other_works': other_works})

@login_required
def rented(request):
    current_user = request.user
    rented = list(RentedWork.objects.filter(user_id = current_user.id, returned = False))
    
    return render(request, 'rental_system/rented.html', {'rented': rented})

def search(query=None):
    queryset = []
    queries = query.split(" ") #
    for search in queries:
        #obj = Work.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
        obj = Work.objects.filter(Q(title__iexact=search) | Q(desc__iexact=search))

        for post in obj:
            queryset.append(post)
    return list(set(queryset))

@login_required
def return_work(request, work_id):
    current_user = request.user
    work = RentedWork.objects.get(user_id = current_user.id, rented_work_id = work_id, returned = False)
    work.returned = True
    work.save()
    return redirect('rented')

@login_required
def rent_work(request, work_id):
    current_user = request.user
    work = Work.objects.get(pk=work_id)
    today = datetime.date.today()
    rentedWorks = RentedWork.objects.all()
    if not rentedWorks.filter(rented_work__id = work_id, returned = False):
        rentedWorks.create(user=current_user, rented_work = work, return_date = today + datetime.timedelta(7))
        return redirect('rented')
    else:
        return redirect('work', work_id)