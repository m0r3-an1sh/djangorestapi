from django.http import HttpResponse
from django.shortcuts import render
from restapi.models import Client,project

# Create your views here.

from restapi.models import Book, Author
from datetime import date

author = Author(name='J.K. Rowlimhvjhvng', email='jkrowling@example.com')
author.save()

book = Book(title='Harry Potter and ', author=author, published_date=date(1997, 6, 26), pages=223)
book.save()

# Retrieve the author for a given book
book = Book.objects.all()
author = book[16].author

def home(request):
    clientobjs = Client.objects.all()
    print(clientobjs[0])
    print(book[16].title)
    print(author.name)
    return HttpResponse("this is home")

from rest_framework import serializers
from rest_framework import status
from .serializer import Clientserializer, Projectserializer, ClientSerializer2,ProjectSerializer2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user

@api_view(['GET','POST'])
def viewclients(request):
    if request.method == "GET":
        clients = Client.objects.all()
        if clients:
            serializer = Clientserializer(clients,many=True)
            serializer = serializer.data[:]
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "POST":
        request.data['created_by']= str(get_user(request))
        serializer = Clientserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def viewclient(request,pk):
    if request.method == "GET":
        client = Client.objects.all().filter(id=pk).values()
        projects = project.objects.filter(clientprojects=client[0]['id']).values('id','projectname')
        data = {"client":client,"project":projects}

        print(data.values())
        # print(projects[0].projectname)
        # print(get_user(request))
        
        if client:
            serializer = ClientSerializer2(data.values(),many=True)
            serializer = serializer.data[:]
            # serializer1 = Projectserializer(projects,many=True)
            # serializer1 = serializer1.data[:]
            # print(serializer1)
            # serializer.append(serializer1)
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

# @api_view([])
# def addclient(request):
#     if request.method == "POST":

# @api_view(['GET','POST'])
# def viewclients(request):
#     if request.method == "GET":
#         clients = Client.objects.all()
#         if clients:
#             serializer = ClientSerializer2(clients,many=True)
#             serializer = serializer.data[:]
#             return Response(serializer)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == "POST":
#         request.data['created_by']= str(get_user(request))
#         serializer = Clientserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
