from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.
from django.http import HttpResponse
from .models import Coin,Collection
from .forms import GradingForm
from django.shortcuts import render,redirect

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
   collections_coin_doesnt_have = Collection.objects.exclude(id__in = coin.collections.all().values_list('id'))
   grading_form = GradingForm()
   return render(request,'coins/detail.html',{
      'coin':coin,'grading_form':grading_form,
      'collections':collections_coin_doesnt_have
   })

def assoc_collection(request, coin_id, collection_id):
   Coin.objects.get(id=coin_id).collections.add(collection_id)
   return redirect('detail',coin_id=coin_id)

def delete_collection(request, coin_id, collection_id):
   Coin.objects.get(id=coin_id).collections.remove(collection_id)
   return redirect('detail',coin_id=coin_id)

def add_grade(request, coin_id):
   form = GradingForm(request.POST)
   if form.is_valid():
      new_grade = form.save(commit=False)
      new_grade.coin_id = coin_id
      new_grade.save()
   return redirect('detail', coin_id=coin_id)

class CoinCreate(CreateView):
   model = Coin
   fields = ['name', 'origin', 'year', 'denom', 'mint']
   success_url = '/coins/'

class CoinUpdate(UpdateView):
  model = Coin
  # Let's disallow the renaming of a coin by excluding the name field!
  fields = ['origin', 'year', 'denom', 'mint']

class CoinDelete(DeleteView):
  model = Coin
  success_url = '/coins/'

class CollectionList(ListView):
   model = Collection

class CollectionDetail(DetailView):
   model = Collection

class CollectionCreate(CreateView):
   model = Collection
   fields = '__all__'

class CollectionUpdate(UpdateView):
   model = Collection
   fields = ['purpose']

class CollectionDelete(DeleteView):
   model = Collection
   success_url = '/collections/'