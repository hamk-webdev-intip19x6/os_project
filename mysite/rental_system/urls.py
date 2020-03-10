from django.urls import path
from django.conf.urls import url
from rental_system import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('type/<str:type_name>', views.type, name='type'),
    path('work/<int:work_id>/', views.work, name='work'),
    path('rented/', views.rented, name='rented'),
    path('account/', views.account, name='account'),
    path('return/<int:work_id>/', views.return_work, name='return_work'),
    path('rent/<int:work_id>/', views.rent_work, name='rent_work'),
    path('test/<int:work_id>/', views.test, name='test'),
    url('password/', views.change_password, name='change_password'),
    path('popular/', views.popular, name='popular'),
    path('reviews/', views.reviews, name='reviews'),
    path('edit_review/<int:rating_id>/', views.edit_review, name='edit_review'),
    path('disable_review/<int:rating_id>/', views.disable_review, name='disable_review'),
    path('all_reviews/<int:work_id>/', views.all_reviews, name="all_reviews")
]