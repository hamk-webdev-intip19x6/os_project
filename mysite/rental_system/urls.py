from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:work_id>/', views.work, name='work'),
]