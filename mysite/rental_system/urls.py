from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work/<int:work_id>/', views.work, name='work'),
    path('rented/', views.rented, name='rented'),
    path('return/<int:work_id>/', views.return_work, name='return_work'),
    path('rent/<int:work_id>/', views.rent_work, name='rent_work'),
    path('test/<int:work_id>/', views.test, name='test')
]