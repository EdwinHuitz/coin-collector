from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
from django.http import HttpResponse
from .models import Coin
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
   grading_form = GradingForm()
   return render(request,'coins/detail.html',{
      'coin':coin,'grading_form':grading_form
   })

def add_grade(request, coin_id):
   form = GradingForm(request.POST)
   if form.is_valid():
      new_grade = form.save(commit=False)
      new_grade.coin_id = coin_id
      new_grade.save()
   return redirect('detail', coin_id=coin_id)

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
