from django.urls import path
from . import views

urlpatterns = [
    
    #Sign In Page
    path('sign_in/', views.sign_in, name='sign_in'),
    
    #LogIn Page
    path('login/', views.log_in, name='log_in'), 
    
    #About Page
    path('about/', views.about, name='about')
]