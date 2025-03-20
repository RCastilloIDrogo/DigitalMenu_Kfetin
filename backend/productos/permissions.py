from rest_framework.permissions import BasePermission

class IsVarona(BasePermission):
    """ Permitir solo a usuarios con el rol 'Varona' administrar productos. """
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Varona'
