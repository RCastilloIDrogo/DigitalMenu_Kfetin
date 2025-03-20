from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('nuevo/', ProductoCreateView.as_view(), name='producto-create'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto-update'), 
    path('<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto-delete'), 
]
