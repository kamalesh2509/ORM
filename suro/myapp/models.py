from django.db import models
from django.contrib import admin
class footballplayers (models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    age=models.IntegerField()
    record=models.IntegerField()
    city=models.CharField(max_length=100)

class playersAdmin(admin.ModelAdmin):
    list_display=('name','address','age','record','city')