from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    placed_date = models.DateField(auto_now_add=True)
    dead_line =models.DateField()
    group = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    placed_date = models.DateField(auto_now_add=True)
    dead_line = models.DateField()
    task_assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)