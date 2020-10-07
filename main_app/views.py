from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
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
class CoinCreate(CreateView):
   model = Coin
   fields = '__all__'
   success_url = '/coins/'
class CoinUpdate(UpdateView):
  model = Coin
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['origin', 'year', 'denom', 'mint']

class CoinDelete(DeleteView):
  model = Coin
  success_url = '/coins/'
