from django.db import models
from django.urls import reverse
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
   def get_absolute_url(self):
      return reverse('detail',kwargs={'coin_id':self.id})