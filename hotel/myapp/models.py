from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=20)
    imageUrl=models.CharField(max_length=100)
    description=models.CharField(max_length=30)
    rating=models.IntegerField()
    cost=models.CharField(max_length=20)
    city=models.CharField(max_length=20,default='')
    country=models.CharField(max_length=20,default='')
    about=models.CharField(max_length=500,default='')
class Explore(models.Model):
    name=models.CharField(max_length=20)
    imageUrl=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    rating=models.IntegerField()
    cost=models.CharField(max_length=20)
    city=models.CharField(max_length=20,default='')
    country=models.CharField(max_length=20,default='')
    about=models.CharField(max_length=500,default='')