from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.DonationListView.as_view(), name='donation_list'),
    path('create/', views.DonationCreateView.as_view(), name='donation_create'),
    path('<int:pk>/', views.DonationDetailView.as_view(), name='donation_detail'),
    path('<int:pk>/update/', views.DonationUpdateView.as_view(), name='donation_update'),
    path('<int:pk>/delete/', views.DonationDeleteView.as_view(), name='donation_delete'),
]
