from django.http import HttpResponse
from django.shortcuts import render
from restapi.models import Client,project

# Create your views here.

def home(request):
    clientobjs = Client.objects.all()
    print(clientobjs[0])
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
            serializer = serializer.data
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
        client = Client.objects.filter(id=pk).all()
        print(client)
        projects = project.objects.filter(clientprojects=client[0].id)
        if len(projects) == 0:
            data = {"id":client[0].id,"clientname":client[0].clientname,"created_at":client[0].created_at,"created_by":client[0].created_by,"project":{"id":None,"projectname":None}}
            print(data)
        else:
            data = {"id":client[0].id,"clientname":client[0].clientname,"created_at":client[0].created_at,"created_by":client[0].created_by,"project":{"id":projects[0].id,"projectname":projects[0].projectname}}
            print(data)
        
        if client:
            serializer = ClientSerializer2(data)
            serializer = serializer.data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        


@api_view([ 'PUT', 'DELETE'])
def clientputdel(request,pk):

    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = Clientserializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def viewprojects(request):
    if request.method == "GET":
        projects = project.objects.all()
        if projects:
            serializer = Projectserializer(projects,many=True)
            serializer = serializer.data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "POST":
        # request.data['created_by']= str(get_user(request))
        serializer = Projectserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





