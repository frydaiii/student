# Create your models here.
from django.db import models


class Student(models.Model):
    id = models.IntegerField(max_length=2, default=0, primary_key=True)
    name = models.CharField(max_length=50, default='')
    class_name = models.CharField(max_length=10, default='')
    mark = models.IntegerField(max_length=3, default=0)
    gender = models.CharField(max_length=6, default='male')

