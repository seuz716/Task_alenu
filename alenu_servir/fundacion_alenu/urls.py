from django.contrib import admin
from django.urls import path
from tasks.views import signup, login, logout, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', home, name='home'),
    # Otras rutas de la aplicación...
]