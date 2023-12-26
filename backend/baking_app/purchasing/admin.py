from django.contrib import admin
from .models import Vendor, StatusCategory, Status, PurchaseOrder, POItem
from config.models import Config
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


currency_symbol = Config.objects.get(item="currency_symbol").value
currency_decimals = int(Config.objects.get(item="currency_decimals").value)

# Register your models here.

admin.site.register(Vendor)
admin.site.register(StatusCategory)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
  list_display = ("name", "category", "sequence")


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
  list_display = ("status", "order_date", "vendor", "item_count", "po_cost")
  list_filter = ("status", "order_date")

  def po_cost(self, obj: PurchaseOrder):
    return f"{currency_symbol}{round(obj.total_cost(), currency_decimals)}"

  def item_count(self, obj: PurchaseOrder):
    url = f"{reverse("admin:purchasing_poitem_changelist")}?{urlencode({"purchase_order__id": f"{obj.id}"})}"
    return format_html('<a href="{}">{} Items</a>', url, obj.poitem_set.all().count())


@admin.register(POItem)
class ItemAdmin(admin.ModelAdmin):
  list_display = ("purchase_order", "ingredient", "purchase_qty")
  list_filter = ("purchase_order",)