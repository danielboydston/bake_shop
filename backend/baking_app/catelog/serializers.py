from rest_framework import serializers
from .models import Product, Variation, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'active']


class VariationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variation
        fields = ['product', 'name', 'cost', 'sale_price', 'active']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'disp_order']
