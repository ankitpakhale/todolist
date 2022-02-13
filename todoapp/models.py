from turtle import title
from django.db import models

# Create your models here.
class TodoList(models.Model):
    title =             models.CharField(max_length=100, default='')
    description =       models.TextField(max_length=1000, default='')
    def __str__(self):
        return str(self.title)