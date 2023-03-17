from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.getEvents, name='get-events'),
    path('create-rent/', views.createRent, name='create-rent')
]