from rest_framework import generics, permissions
from .models import Mesa
from .serializers import MesaSerializer

class IsAdmin(permissions.BasePermission):
    """ Permitir solo a administradores gestionar mesas """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

# Vista para listar todas las mesas
class MesaListView(generics.ListAPIView):
    queryset = Mesa.objects.all().order_by('numero')
    serializer_class = MesaSerializer
    permission_classes = [permissions.AllowAny]  # Cualquiera puede ver las mesas

# Vista para que el admin cree nuevas mesas
class MesaCreateView(generics.CreateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    permission_classes = [IsAdmin]  # Solo admin puede crear mesas

# Vista para actualizar el estado de una mesa (ocupada/disponible)
class MesaUpdateEstadoView(generics.UpdateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    permission_classes = [IsAdmin]  # Solo admin puede modificar el estado
