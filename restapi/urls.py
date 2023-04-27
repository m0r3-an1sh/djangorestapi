from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('h', views.home , name='home'),
    path('clients/',views.viewclients,name='viewclients'),
    path('client/<int:pk>/',views.viewclient,name='viewclient'),
    path('clientsputpatch/<int:pk>/',views.clientputdel,name='clientputdel'),
    path('projectsadd/',views.viewprojects,name="viewprojects"),
]