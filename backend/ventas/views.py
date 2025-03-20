from django.db.models import Sum
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now, timedelta
from .models import Venta, DetalleVenta
from .serializers import VentaSerializer, VentaCreateSerializer

# 📌 Permiso para meseros (registrar ventas)
class IsMesero(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'mesero'

# 📌 Vista para registrar una venta en el cafetín
class VentaCreateView(generics.CreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaCreateSerializer
    permission_classes = [IsMesero]

    def perform_create(self, serializer):
        serializer.save(cajero=self.request.user)

# 📌 Vista para listar todas las ventas (para reportes)
class VentaListView(generics.ListAPIView):
    queryset = Venta.objects.all().order_by('-fecha_creacion')
    serializer_class = VentaSerializer
    permission_classes = [permissions.IsAuthenticated]

# 📌 Vista para obtener detalles de una venta específica
class VentaDetailView(generics.RetrieveAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [permissions.IsAuthenticated]

# 📌 Vista para generar reportes de ventas diarias y semanales
class ReporteVentasView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, formato='dia'):
        fecha_actual = now()
        fecha_inicio = fecha_actual - timedelta(days=7) if formato == 'semana' else fecha_actual.replace(hour=0, minute=0, second=0)

        ventas = Venta.objects.filter(fecha_creacion__gte=fecha_inicio)
        total_ingresos = ventas.aggregate(total=Sum('total'))['total'] or 0

        reporte = {
            "total_ventas": ventas.count(),
            "total_ingresos": total_ingresos,
            "detalles": VentaSerializer(ventas, many=True).data
        }
        return Response(reporte)
