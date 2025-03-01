from django.urls import path
from . import views

urlpatterns = [
    # Paths for Categories
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add_categories/', views.add_categories, name='add_categories'),  
    path('categories/edit_categories/<int:pk>/', views.edit_categories, name='edit_categories'),
    path('categories/delete_categories/<int:pk>/', views.delete_categories, name='delete_categories'),
    
    # Paths for Posts
    path('posts/',views.posts,name="posts"),
    path('posts/add/',views.add_posts,name="add_posts"),
    path('posts/delete/<int:pk>/', views.delete_posts, name='delete_posts'),

    #user
    path('users/', views.users, name='users'),  
    path('users/add/', views.add_users, name='add_users'),  
    path('users/edit/<int:pk>/', views.edit_user, name='edit_users'),
    path('users/delete/<int:pk>/',views.delete_user,name='delete_user'),

]
