from django.db import models

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    counts =models.IntegerField()

class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=150)
    
