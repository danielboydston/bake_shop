from django.contrib import admin
from .models import Product, Category, Variation, VariationPackaging, VariationAddOn
from config.models import Config
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

currency_symbol = Config.objects.get(item="currency_symbol").value
currency_decimals = int(Config.objects.get(item="currency_decimals").value)

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ("name", "variations", "category")

  def variations(self, obj:Product):
    count = obj.variation_set.count()
    url = f"{reverse("admin:catelog_variation_changelist")}?{urlencode({"product__id": f"{obj.id}"})}"
    return format_html('<a href="{}">{} Variations</a>', url, count)
  


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
  list_display = ("display_name", "unit_cost", "sale_price_display")
  list_filter = ("product",)

  def display_name(self, obj):
    return f"{obj.product} {obj.name}"

  def unit_cost(self, obj):
    return f"{currency_symbol}{round(obj.unit_cost(), currency_decimals)}"
  
  def sale_price_display(self, obj):
    return f"{currency_symbol}{round(obj.sale_price, currency_decimals)}"
  

@admin.register(VariationPackaging)
class VariationPackagingAdmin(admin.ModelAdmin):
  list_display = ("variation","ingredient", "qty")


admin.site.register(VariationAddOn)
