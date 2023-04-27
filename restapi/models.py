from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Client(models.Model):
      id = models.AutoField(primary_key=True)
      clientname = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add=True)
      created_by = models.CharField(max_length=255)
      def __str__(self) -> str:
          return self.clientname

class project(models.Model):
      id = models.AutoField(primary_key=True)
      projectname = models.CharField(max_length=255)
      users = models.ForeignKey(User,on_delete=models.CASCADE)
      clientprojects = models.ForeignKey(Client,on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    pages = models.IntegerField()
