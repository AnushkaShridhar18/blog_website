from django.urls import path
from . import views

app_name = 'blogs'  # Namespace the URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('blog/<slug:slug>/', views.blogs, name='blogs'),
]
