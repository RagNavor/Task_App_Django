from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.




class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    placed_date = models.DateField(auto_now_add=True)
    dead_line =models.DateField()
    estado = models.CharField(max_length=13, default='En desarrollo')
    created_by_user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    placed_date = models.DateField(auto_now_add=True)
    dead_line = models.DateField()
    estado = models.CharField(max_length=13, default='En desarrollo')
    def __str__(self):
        return self.name