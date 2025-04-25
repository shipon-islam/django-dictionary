from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
]
