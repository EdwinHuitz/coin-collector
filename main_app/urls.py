from django.urls import path
from . import views

urlpatterns=[
   #views.* defines which function will be called on the views page
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('coins/',views.coins_index,name='index'),
   path('coins/<int:coin_id>/', views.coins_detail, name='detail'),
]