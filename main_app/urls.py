from django.urls import path
from . import views

urlpatterns=[
   #views.* defines which function will be called on the views page
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('cats/',views.coins_index,name='index'),
]