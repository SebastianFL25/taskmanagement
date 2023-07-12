from django.db import models
from base.models import User

class Status(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    
    title= models.CharField(max_length=250)
    Description=models.TextField()
    due_date=models.DateTimeField(auto_now=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.ForeignKey(Status,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    