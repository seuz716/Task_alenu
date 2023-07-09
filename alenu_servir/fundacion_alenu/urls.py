from django.contrib import admin
from django.urls import path, include
from tasks.views import signup, user_login, user_logout, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('donations/', include('donations.urls')),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', home, name='home'),
    # Otras rutas de la aplicación...
]
