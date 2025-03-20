from django.urls import path
from .views import VentaCreateView, VentaListView, VentaDetailView, ReporteVentasView

urlpatterns = [
    path('', VentaListView.as_view(), name='venta-list'),
    path('nueva/', VentaCreateView.as_view(), name='venta-create'),
    path('<int:pk>/', VentaDetailView.as_view(), name='venta-detail'),
    path('reporte/<str:formato>/', ReporteVentasView.as_view(), name='reporte-ventas'),
]
