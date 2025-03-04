from rest_framework import generics, permissions
from .models import Categoria, Plato
from .serializers import CategoriaSerializer, PlatoSerializer

# Solo administradores pueden modificar el menú
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

# Vista para listar y crear categorías
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminUser]  # Solo Admins

# Vista para editar y eliminar categorías
class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminUser]  # Solo Admins

# Vista para listar y crear platos
class PlatoListCreateView(generics.ListCreateAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [IsAdminUser]  # Solo Admins

# Vista para editar y eliminar platos
class PlatoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [IsAdminUser]  # Solo Admins
