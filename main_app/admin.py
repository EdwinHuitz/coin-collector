from django.contrib import admin
from .models import Coin, Grading

# Register your models here.
admin.site.register(Coin)
admin.site.register(Grading)