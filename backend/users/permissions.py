from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Permiso personalizado para permitir solo a los administradores realizar ciertas acciones.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser
