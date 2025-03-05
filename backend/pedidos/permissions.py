from rest_framework import permissions

class IsMesero(permissions.BasePermission):
    """Permiso para que solo los meseros puedan acceder a ciertos endpoints."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'mesero'

class IsCocinero(permissions.BasePermission):
    """Permiso para que solo los cocineros puedan acceder a ciertos endpoints."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'cocinero'

class IsAdmin(permissions.BasePermission):
    """Permiso para que solo los administradores puedan acceder a ciertos endpoints."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
