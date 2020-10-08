from django.urls import path
from . import views

urlpatterns=[
   #views.* defines which function will be called on the views page
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('coins/',views.coins_index,name='index'),
   path('coins/<int:coin_id>/', views.coins_detail, name='detail'),
   path('coins/create/',views.CoinCreate.as_view(),name='coins_create'),
   path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coins_update'),
   path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coins_delete'),
   path('coins/<int:coin_id>/add_grade/', views.add_grade, name='add_grade'),
   path('coins/<int:coin_id>/assoc_collection/<int:collection_id>/', views.assoc_collection, name='assoc_collection'),
   path('coins/<int:coin_id>/delete_collection/<int:collection_id>/',views.delete_collection, name='delete_collection'),
   path('collections/', views.CollectionList.as_view(), name='collections_index'),
   path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collections_detail'),
   path('collections/create/', views.CollectionCreate.as_view(), name='collections_create'),
   path('collections/<int:pk>/update/', views.CollectionUpdate.as_view(), name='collections_update'),
   path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collections_delete'),
]