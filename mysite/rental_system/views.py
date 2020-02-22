from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from operator import attrgetter
from .models import Work, Type, RentedWork


def index(request):
    works = Work.objects.all()
    types = Type.objects.all()
    context = {'works': works, 'types': types}

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
    rented = RentedWork.objects.filter(rented_work = work_id);
    return render(request, 'rental_system/work.html', {'work': work, 'rented': rented})

def rented(request):
    current_user = request.user
    rented = list(RentedWork.objects.filter(user_id = current_user.id))
    
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