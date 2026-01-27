from django.urls import path
from . import views

urlpatterns = [
    #Adding Journal
    path('add/', views.add, name='add'),
    
]