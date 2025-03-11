from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Prefijo claro para "users"
    path('api/auth/', include('users.urls')),  # ✅ Esto debe estar presente
    path('api/menu/', include('menu.urls')),  # Prefijo claro y ya correcto para "menu"
    path('api/pedidos/', include('pedidos.urls')),  # Prefijo claro para "pedidos"
    path('api/mesas/', include('mesas.urls')),  # Prefijo claro para "mesas"
]

# Agregar las rutas para archivos estáticos y multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
