
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.dictionary, name=''),
    path('dictionary/<int:dictionaryId>/',views.dictionary_by_id, name='dictionary_by_id'),
    path('dictionary/search/', views.search_dictionary, name='search_dictionary'),
    path('dictionary/filter/', views.filter_dictionary, name='filter_dictionary'),
    
]