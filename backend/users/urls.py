from django.urls import path
from .views import CustomTokenObtainPairView, UserListCreateView, UserManagementView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListCreateView.as_view(), name='user_list'),  # Ver y crear usuarios
    path('users/<int:pk>/', UserManagementView.as_view(), name='user_detail'),  # Editar/eliminar usuario
]
