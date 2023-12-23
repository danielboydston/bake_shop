from django.contrib import admin
from .models import Product, Category, Variation, VariationPackaging, VariationAddOn

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Variation)
admin.site.register(VariationPackaging)
admin.site.register(VariationAddOn)
