from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('h', views.home , name='home'),
    path('all/',views.viewclients,name='viewclients'),
    path('client/<int:pk>/',views.viewclient,name='viewclient'),
]