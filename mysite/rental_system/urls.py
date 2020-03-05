from django.urls import path
from django.conf.urls import url
from rental_system import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work/<int:work_id>/', views.work, name='work'),
    path('rented/', views.rented, name='rented'),
    path('account/', views.account, name='account'),
    path('return/<int:work_id>/', views.return_work, name='return_work'),
    path('rent/<int:work_id>/', views.rent_work, name='rent_work'),
    path('test/<int:work_id>/', views.test, name='test'),
    url('password/', views.change_password, name='change_password')
]