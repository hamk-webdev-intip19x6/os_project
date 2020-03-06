from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Q
from operator import attrgetter
from .models import Work, Type, Genre, RentedWork, Rating
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from django.core.paginator import Paginator
from django.core.exceptions import EmptyResultSet
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from django.core import serializers
from django.db.models import Count

from .forms import RatingForm

def index(request):
    works = Work.objects.order_by('-pub_date').all()
    types = Type.objects.all()
    genres = Genre.objects.all()
    if not request.GET.get('search'):
        paginator = Paginator(works, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = works

    context = {'works': page_obj, 'types': types, 'genres': genres}

    #search
    query = ""
    if request.GET.get('search'):
        query = request.GET['search']
        context['query'] = str(query)
    
    posts = sorted(search(query), key=attrgetter('title'), reverse=True)
    context['posts'] = posts
    return render(request, 'rental_system/index.html', context)

def work(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    ratings = Rating.objects.filter(work_id = work_id).all()
    creators = work.creators.all()
    other_works = list(Work.objects.filter(~Q(id = work_id),creators__in=creators))[:5]
    rented = RentedWork.objects.all()

    form = RatingForm()

    if rented.filter(rented_work_id = work_id).exists():
        returned = rented.filter(rented_work_id = work_id, returned=False).order_by('-rent_date').first()
    else:
        returned = False
        
    commented = False
    if not request.user.is_anonymous:
        user = request.user
        if ratings.filter(user_id = user, work_id = work_id, visible = True):
            commented = True


    if request.method == 'POST':
        ratings = Rating.objects.all()
        if not commented:
            form = RatingForm(request.POST)
            if form.is_valid():
                work = Work.objects.get(pk = work_id)
                ratings.create(user=user, work=work, rating=form.cleaned_data['rating'], comment=form.cleaned_data['comment'])
        return redirect('work', work_id)



    return render(request, 'rental_system/work.html', {'work': work, 'rented': returned, 'other_works': other_works, 'ratings': ratings, 'form':form, 'commented': commented})

@login_required
def reviews(request):
    user = request.user
    ratings = Rating.objects.filter(user_id = user, visible = True).order_by('post_date').all()

    return render(request, 'rental_system/reviews.html', {'comments': ratings})

@login_required
def disable_review(request, rating_id):
    current_user = request.user
    rating = Rating.objects.get(user_id = current_user.id, pk = rating_id)
    rating.visible = False
    rating.save()
    return redirect('reviews')

@login_required
def edit_review(request, rating_id):
    user = request.user
    ratings = Rating.objects.get(user_id = user, pk = rating_id)
    form = RatingForm(initial={'comment': ratings.comment, 'rating': ratings.rating})
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            ratings.comment = form.cleaned_data['comment']
            ratings.rating = form.cleaned_data['rating']
            ratings.visible = form.cleaned_data['visible']
            ratings.save()
        return redirect('reviews')
    return render(request, 'rental_system/edit_review.html', {'reviews': ratings, 'form':form})

@login_required
def rented(request):
    current_user = request.user
    rented = list(RentedWork.objects.filter(user_id = current_user.id, returned = False))
    
    return render(request, 'rental_system/rented.html', {'rented': rented})

@login_required
def account(request):
    current_user = request.user
    #account = list(RentedWork.objects.filter(user_id = current_user.id, returned = False))
    return render(request, 'rental_system/account.html', {'account': account})

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
    work.date_returned = timezone.now()
    work.save()
    return redirect('rented')

@login_required
def rent_work(request, work_id):
    current_user = request.user
    work = Work.objects.get(pk=work_id)
    time = timezone.now() + datetime.timedelta(days=30)
    rentedWorks = RentedWork.objects.all()
    if not rentedWorks.filter(rented_work__id = work_id, returned = False):
        rentedWorks.create(user=current_user, rented_work = work, return_date = time)
        return redirect('rented')
    else:
        return redirect('work', work_id)

def test(request, work_id):
    rented = RentedWork.objects.all()
    data = serializers.serialize('json', rented)
    return render(request, 'rental_system/test.html', {'data': data})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
def popular(request):
    rented = list(RentedWork.objects.values('rented_work__title').annotate(count=Count('id')).values('count', 'rented_work__title', 'rented_work__id').order_by('-count').filter(count__gt=1)[:5])
    return render(request, 'rental_system/popular.html', {'data': rented})
