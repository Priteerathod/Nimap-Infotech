from django.db import models

# Create your models here.

class Client(models.Model):
    client_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=50)
    
def __str__(self):
    return self.client_name

class Project(models.Model):
    name=models.CharField(max_length=100)
    projects=models.ForeignKey(Client,on_delete=models.CASCADE)
   