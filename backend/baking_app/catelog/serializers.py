from rest_framework import serializers
from .models import Product, Variation, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'disp_order']


class VariationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Variation
        fields = ['product', 'name', 'cost', 'sale_price', 'active']


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'active']
