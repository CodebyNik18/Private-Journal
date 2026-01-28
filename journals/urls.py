from django.urls import path
from . import views

urlpatterns = [
    #Adding Journal
    path('add/', views.add, name='add'),
    
    #Edit Journal
    path('edit_journal/<int:pk>', views.edit_journal, name="edit_journal"),
    
    #Delete Journal
    path('delete_journal/<int:pk>', views.delete_journal, name="delete_journal")
    
]