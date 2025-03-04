from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        extra_kwargs = {'role': {'required': True}}  # El rol es obligatorio

    def create(self, validated_data):
        # Asegurar que solo el Admin pueda crear usuarios
        request = self.context.get('request')
        if request and not request.user.is_superuser:
            raise serializers.ValidationError("Solo los administradores pueden crear usuarios.")

        # Crear usuario con role mesero o cocinero
        role = validated_data.get('role')
        if role not in ["mesero", "cocinero"]:
            raise serializers.ValidationError("Solo puedes crear usuarios con roles 'mesero' o 'cocinero'.")

        return User.objects.create_user(**validated_data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role if user.role else "undefined"  # Asegurar que no sea None
        return token


