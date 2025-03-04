from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # <-- Importar settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Ahora "users" maneja autenticación
    path('api/menu/', include('menu.urls')),  # Gestión del menú
]

# Agregar las rutas para archivos estáticos y multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
