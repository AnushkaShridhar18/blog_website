from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from blogs import views  # Import views from the blogs app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('category/', include('blogs.urls', namespace='blogs')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('blogs/search/', views.search, name='search'),
    path('register/', views.register, name='register'),  # Fixed missing slash for consistency
    path('login/', views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('dashboard/', include('dashboard.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
