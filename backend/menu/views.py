from rest_framework import generics, permissions
from .models import Categoria, Plato
from .serializers import CategoriaSerializer, PlatoSerializer

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

# ✅ Vista para listar y crear categorías
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminUser]  # Solo Admins pueden crear categorías

# ✅ Vista para editar, ver y eliminar una categoría
class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):  # 🔹 Esta vista debe existir
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminUser]  # Solo Admins pueden modificar categorías

class PlatoListView(generics.ListAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [permissions.AllowAny]  # 🔹 Permitir acceso sin autenticación

# ✅ Vista protegida para crear platos
class PlatoListCreateView(generics.ListCreateAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [IsAdminUser]  # Solo Admins pueden crear

# ✅ Vista protegida para modificar platos
class PlatoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [IsAdminUser]  # Solo Admins pueden modificar
