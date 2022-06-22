from django.db import models

# Create your models here.

class Bag(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    cost = models.IntegerField()
    image = models.CharField(default=None, blank=True, null=True, max_length=2000)
