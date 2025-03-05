from django.urls import path
from .views import MesaListCreateView, MesaDetailView

urlpatterns = [
    path('mesas/', MesaListCreateView.as_view(), name='mesa-list'),
    path('mesas/<int:pk>/', MesaDetailView.as_view(), name='mesa-detail'),
]
