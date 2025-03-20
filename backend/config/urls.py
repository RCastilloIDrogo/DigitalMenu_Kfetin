from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/auth/', include('users.urls')),
    path('api/menu/', include('menu.urls')),
    path('api/pedidos/', include('pedidos.urls')),
    path('api/mesas/', include('mesas.urls')),
    path('api/ventas/', include('ventas.urls')),
    path('api/productos/', include('productos.urls')), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
