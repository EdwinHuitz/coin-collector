from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Coin

#home page
def home(request):
   return render(request,'index.html')
#about page
def about(request):
   return render(request,'about.html')
#all coins page
def coins_index(request):
   coins=Coin.objects.all()
   return render(request,'coins/index.html',{'coins': coins})
def coins_detail(request, coin_id):
  coin = Coin.objects.get(id=coin_id)
  return render(request, 'coins/detail.html', { 'coin': coin })