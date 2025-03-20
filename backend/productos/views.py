from rest_framework import generics, permissions
from .models import Producto
from .serializers import ProductoSerializer
from .permissions import IsVarona

class ProductoListView(generics.ListAPIView):
    queryset = Producto.objects.all().order_by('-fecha_creacion')
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductoCreateView(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsVarona]

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)

class ProductoUpdateView(generics.UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsVarona]

class ProductoDeleteView(generics.DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsVarona]
