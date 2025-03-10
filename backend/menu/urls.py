from django.urls import path
from .views import CategoriaListCreateView, CategoriaDetailView, PlatoListView, PlatoListCreateView, PlatoDetailView

urlpatterns = [
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),  # 🔹 Asegúrate de que esta línea existe

    path('platos/', PlatoListView.as_view(), name='plato-list'),  # 🔹 Vista pública
    path('platos/admin/', PlatoListCreateView.as_view(), name='plato-create'),  # 🔹 Solo Admins pueden crear
    path('platos/<int:pk>/', PlatoDetailView.as_view(), name='plato-detail'),  # 🔹 Solo Admins pueden modificar
]
