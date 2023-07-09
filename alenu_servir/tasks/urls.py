from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]
