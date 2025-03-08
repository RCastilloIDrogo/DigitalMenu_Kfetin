from django.db.models import Count
from django.contrib.auth import get_user_model  # Importamos el modelo User
from rest_framework import generics, permissions
from .models import Pedido, DetallePedido
from .serializers import PedidoSerializer, PedidoCreateSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


# Solo los meseros pueden crear pedidos
class IsMesero(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'mesero'

# Solo los cocineros pueden actualizar pedidos
class IsCocinero(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'cocinero'

# Los meseros pueden crear y listar pedidos
class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all().order_by('-fecha_creacion')
    serializer_class = PedidoCreateSerializer
    permission_classes = [IsMesero]  # Solo meseros pueden acceder

    def perform_create(self, serializer):
        serializer.save(mesero=self.request.user)

# Los cocineros pueden actualizar el estado de un pedido
class PedidoUpdateView(generics.UpdateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsCocinero]  # Solo cocineros pueden modificar pedidos

# Vista para ver detalles de un pedido
class PedidoDetailView(generics.RetrieveAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PedidoListView(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'mesero':
            return Pedido.objects.filter(mesero=user).order_by('-fecha_creacion')
        elif user.role == 'cocinero':
            return Pedido.objects.filter(estado__in=['pendiente', 'en_preparacion']).order_by('-fecha_creacion')
        return Pedido.objects.none()

class PedidoHistorialView(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(estado='listo').order_by('-fecha_creacion')
    
class ClientePedidoCreateView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoCreateSerializer
    permission_classes = [permissions.AllowAny]  # Permitir a cualquier usuario hacer pedidos

    def perform_create(self, serializer):
        # Buscar un mesero disponible (puede ser el que tenga menos pedidos asignados)
        mesero_disponible = User.objects.filter(role="mesero").annotate(
            num_pedidos=Count('pedidos')
        ).order_by('num_pedidos').first()  # Mesero con menos pedidos asignados

        if mesero_disponible:
            serializer.save(mesero=mesero_disponible)  # Asignar el mesero disponible
        else:
            serializer.save(mesero=None)  # Si no hay meseros, se deja vacío (caso poco probable)
    


