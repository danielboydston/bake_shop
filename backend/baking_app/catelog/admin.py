from django.contrib import admin
from .models import Product, Category, Variation, VariationPackaging, VariationAddOn

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ("name", "category")


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
  list_display = ("display_name", "unit_cost", "sale_price")

  def display_name(self, obj):
    return f"{obj.product} {obj.name}"

  def unit_cost(self, obj):
    return f"{obj.unit_cost():.0f}"


@admin.register(VariationPackaging)
class VariationPackagingAdmin(admin.ModelAdmin):
  list_display = ("variation","ingredient", "qty", "unit")


admin.site.register(VariationAddOn)
