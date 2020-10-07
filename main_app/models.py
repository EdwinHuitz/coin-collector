from django.db import models

# Create your models here.
#name, origin, year, denom, mint
class Coin(models.Model):
   name = models.CharField(max_length=100)
   origin = models.CharField(max_length=100)
   year = models.IntegerField()
   denom = models.CharField(max_length=100)
   mint = models.CharField(max_length=100)
   def __str__(self):
      return self.name