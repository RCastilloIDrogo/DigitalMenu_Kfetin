from rest_framework import generics, permissions
from .models import Mesa
from .serializers import MesaSerializer
from users.permissions import IsAdmin  # Usa import absoluto (recomendado)



class MesaListCreateView(generics.ListCreateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    permission_classes = [IsAdmin]  # Solo el Admin puede gestionar mesas

class MesaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    permission_classes = [IsAdmin]  # Solo el Admin puede gestionar mesas
