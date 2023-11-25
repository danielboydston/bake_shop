from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer, VariationSerializer, CategorySerializer
from .models import Product, Variation, Category


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class VariationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product variations to be viewed or edited.
    """
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]