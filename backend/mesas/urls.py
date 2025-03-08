# Dentro de la carpeta de tu aplicación de mesas
from django.urls import path
from .views import MesaListView, MesaCreateView, MesaUpdateEstadoView

urlpatterns = [
    path('', MesaListView.as_view(), name='mesa-lista'),  # Listar mesas
    path('crear/', MesaCreateView.as_view(), name='mesa-crear'),  # Crear mesa
    path('<int:pk>/estado/', MesaUpdateEstadoView.as_view(), name='mesa-estado'),  # Cambiar estado
]
