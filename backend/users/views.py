from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]  # Solo el Admin puede acceder

    def create(self, request, *args, **kwargs):
        # Verificar si el usuario que hace la petición es un administrador
        if not request.user.is_superuser:
            return Response(
                {"error": "Solo los administradores pueden crear usuarios."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Solo permitir la creación de Meseros y Cocineros
        role = request.data.get("role")
        if role not in ["mesero", "cocinero"]:
            return Response(
                {"error": "Solo puedes crear usuarios con roles 'mesero' o 'cocinero'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Obtener usuario autenticado
        user = User.objects.get(username=request.data.get("username"))

        # Agregar el role a la respuesta y asegurar que no sea vacío
        response.data['role'] = user.role if user.role else "undefined"

        return response


