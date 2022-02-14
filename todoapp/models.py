from turtle import title
from django.db import models

# Create your models here.

class signUp(models.Model):
    name =                  models.CharField(max_length=30, default='')
    email =                 models.EmailField(default='')
    number =                models.PositiveIntegerField(default='')
    password =              models.CharField(default='', max_length=15)
    confirmPassword =       models.CharField(default='', max_length=15)
    def __str__(self):
        return self.name
    

class TodoList(models.Model):
    title =                 models.CharField(max_length=100, default='')
    description =           models.TextField(max_length=1000, default='')
    owner  =                models.ForeignKey(signUp, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
