from django.db.models import fields
from rest_framework import serializers
from .models import Client,project


class Projectserializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ("id","projectname","users")

class Clientserializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id","clientname","created_at","created_by")

class ProjectSerializer2(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ("id","projectname")

class ClientSerializer2(serializers.ModelSerializer):
    project = ProjectSerializer2()
    class Meta:
        model = Client
        fields = ("id","clientname","created_at","created_by","project")
    


