from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.
from django.http import HttpResponse
from .models import Coin,Collection
from .forms import GradingForm
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#home page
def home(request):
   return render(request,'index.html')

#about page
def about(request):
   return render(request,'about.html')

@login_required
#all coins page
def coins_index(request):
   coins=Coin.objects.filter(user=request.user)
   #alternative is coins=request.user.coin_set.all()
   return render(request,'coins/index.html',{'coins': coins})

@login_required
def coins_detail(request, coin_id):
   coin = Coin.objects.get(id=coin_id)
   collections_coin_doesnt_have = Collection.objects.exclude(id__in = coin.collections.all().values_list('id'))
   grading_form = GradingForm()
   return render(request,'coins/detail.html',{
      'coin':coin,'grading_form':grading_form,
      'collections':collections_coin_doesnt_have
   })

@login_required
def assoc_collection(request, coin_id, collection_id):
   Coin.objects.get(id=coin_id).collections.add(collection_id)
   return redirect('detail',coin_id=coin_id)

@login_required
def delete_collection(request, coin_id, collection_id):
   Coin.objects.get(id=coin_id).collections.remove(collection_id)
   return redirect('detail',coin_id=coin_id)

@login_required
def add_grade(request, coin_id):
   form = GradingForm(request.POST)
   if form.is_valid():
      new_grade = form.save(commit=False)
      new_grade.coin_id = coin_id
      new_grade.save()
   return redirect('detail', coin_id=coin_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class CoinCreate(CreateView):
   model = Coin
   fields = ['name', 'origin', 'year', 'denom', 'mint']
   # This inherited method is called when a
   # valid cat form is being submitted
   def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class CoinUpdate(LoginRequiredMixin,UpdateView):
  model = Coin
  # Let's disallow the renaming of a coin by excluding the name field!
  fields = ['origin', 'year', 'denom', 'mint']

class CoinDelete(LoginRequiredMixin,DeleteView):
  model = Coin
  success_url = '/coins/'

class CollectionList(LoginRequiredMixin,ListView):
   model = Collection

class CollectionDetail(LoginRequiredMixin,DetailView):
   model = Collection

class CollectionCreate(LoginRequiredMixin,CreateView):
   model = Collection
   fields = '__all__'

class CollectionUpdate(LoginRequiredMixin,UpdateView):
   model = Collection
   fields = ['purpose']

class CollectionDelete(LoginRequiredMixin,DeleteView):
   model = Collection
   success_url = '/collections/'