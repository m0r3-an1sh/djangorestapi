from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.project)
admin.site.register(models.Book)
admin.site.register(models.Author)
