from django.contrib import admin
from .models import Product, Category, Variation

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Variation)
