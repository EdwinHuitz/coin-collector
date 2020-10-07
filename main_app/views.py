from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Coin:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, origin, year, denom, mint):
   self.name = name
   self.origin = origin
   self.year = year
   self.denom = denom
   self.mint = mint

coins = [
  Coin('Washington Quarter','USA', '1999','25c', 'Denver'),
  Coin('Silver Eagle','USA', '2018','$1', 'Westpoint'),
  Coin('American Innovation','USA', '2020', '$1', 'Philadelphia')
]

#home page
def home(request):
   return render(request,'index.html')
#about page
def about(request):
   return render(request,'about.html')
#all coins page
def coins_index(request):
   return render(request,'coins/index.html',{'coins': coins})
