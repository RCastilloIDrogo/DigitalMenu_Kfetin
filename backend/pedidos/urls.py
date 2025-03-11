from django.urls import path
from .views import (
    PedidoListCreateView,
    PedidoUpdateView,
    PedidoDetailView,
    PedidoHistorialView,
    ClientePedidoCreateView,
    PedidoUpdateEstadoView,
)

urlpatterns = [
    path('', PedidoListCreateView.as_view(), name='pedido-list'),  # /api/pedidos/
    path('<int:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),
    path('<int:pk>/update/', PedidoUpdateView.as_view(), name='pedido-update'),
    path('historial/', PedidoHistorialView.as_view(), name='pedido-historial'),
    path('cliente/', ClientePedidoCreateView.as_view(), name='cliente-pedido-create'),  # ✅ /api/pedidos/cliente/
    path('<int:pk>/estado/', PedidoUpdateEstadoView.as_view(), name='pedido-estado'),
]

