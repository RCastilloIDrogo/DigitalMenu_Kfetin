from django.urls import path
from .views import (
    PedidoListCreateView,
    PedidoUpdateView,
    PedidoDetailView,
    PedidoHistorialView,
    ClientePedidoCreateView,
    PedidoUpdateEstadoView  # Asegúrate de que esta vista esté correctamente definida en views.py
)

urlpatterns = [
    path('pedidos/', PedidoListCreateView.as_view(), name='pedido-list'),
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),
    path('pedidos/<int:pk>/update/', PedidoUpdateView.as_view(), name='pedido-update'),
    path('pedidos/historial/', PedidoHistorialView.as_view(), name='pedido-historial'),
    path('pedidos/cliente/', ClientePedidoCreateView.as_view(), name='cliente-pedido-create'),
    path('pedidos/<int:pk>/estado/', PedidoUpdateEstadoView.as_view(), name='pedido-estado'),
]
