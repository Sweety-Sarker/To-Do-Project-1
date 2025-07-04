from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customuserModel(AbstractUser):
    full_name=phone=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to='media/image',null=True)
    address=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    city_name=models.CharField(max_length=100,null=True)
    bio=models.TextField(null=True)
    phone=models.CharField(max_length=100,null=True)



class todoModel(models.Model):
    user=models.ForeignKey(customuserModel,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    status=models.CharField(null=True,choices=[
        ('pending','pending'),
        ('completed','completed'),
        ('inprogress','inprogress'),
    ])
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)