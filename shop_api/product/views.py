from rest_framework import viewsets
from review.permissions import IsAuthorOrReadOnly
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('create'):
            permissions = [IsAuthenticated]
        elif self.action in ('update', 'partial_update', 'destroy', 'create'):
            permissions = [IsAuthorOrReadOnly]
        else:
            permissions = [AllowAny]
        return [permissions() for permission in permissions]


class CategoryView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
