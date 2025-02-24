from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add_categories/', views.add_categories, name='add_categories'),  
    path('categories/edit_categories/<int:pk>/', views.edit_categories, name='edit_categories'),
     path('categories/delete_categories/<int:pk>/', views.delete_categories, name='delete_categories'),
]
