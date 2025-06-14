from django.urls import path
from . import views

urlpatterns = [
    path('mision/', views.mision_view, name='nuestra_mision'),
    path('programas/', views.programas_view, name='programas'),
    path('transparencia/', views.transparencia_view, name='transparencia'),
    path('participa/', views.participa_view, name='participa'),
    path('contacto/', views.contacto_view, name='contacto'),
]
