from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
# Create your models here.

    
class Author(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    bio=models.TextField()
    #def __str__(self):
    #return self.name
class Category(models.Model):
    Category=models.CharField(max_length=50)
    description=models.TextField()
    #def __str__(self):
    #return self.category
class Article(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="images/")
    content=models.TextField(max_length=6000)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    #def __str__(self):
    #return self.title


