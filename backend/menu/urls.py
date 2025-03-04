from django.urls import path
from .views import CategoriaListCreateView, CategoriaDetailView, PlatoListCreateView, PlatoDetailView

urlpatterns = [
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
    path('platos/', PlatoListCreateView.as_view(), name='plato-list'),
    path('platos/<int:pk>/', PlatoDetailView.as_view(), name='plato-detail'),
]
