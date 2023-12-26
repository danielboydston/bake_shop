from django.contrib import admin
from .models import Order, Item, Status, Customer, ItemAddOn
from config.models import Config
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

currency_symbol = Config.objects.get(item="currency_symbol").value
currency_decimals = int(Config.objects.get(item="currency_decimals").value)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ("status", "order_date", "customer", "item_count", "total_price")
  list_filter = ("order_date","status")

  def item_count(self, obj:Order):
    url = f"{reverse("admin:sales_item_changelist")}?{urlencode({"order__id": f"{obj.id}"})}"
    return format_html('<a href="{}">{} Items</a>', url, obj.item_set.all().count())
  
  def total_price(self, obj:Order):
    return f"{currency_symbol}{round(obj.total_price(), currency_decimals)}"
  

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  list_display = ("order", "product_variation", "qty", "unit", "unit_price_display")
  list_filter = ("order",)

  def unit_price_display(self, obj: Item):
    return f"{currency_symbol}{round(obj.unit_price, currency_decimals)}"

admin.site.register(Status)
admin.site.register(Customer)


@admin.register(ItemAddOn)
class ItemAddOnAdmin(admin.ModelAdmin):
  list_display = ("item", "ingredient", "qty", "unit", "unit_price_display")
  list_filter = ("item",)

  def unit_price_display(self, obj: ItemAddOn):
    return f"{currency_symbol}{round(obj.unit_price, currency_decimals)}"