from django.contrib import admin
from .models import Order, Item, Status, Customer, ItemAddOn

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ("status", "order_date", "customer", "item_count", "total_price")
  list_filter = ("order_date","status")

  def item_count(self, obj:Order):
    return len(obj.item_set.all())
  
  def total_price(self, obj:Order):
    total = 0
    for item in obj.item_set.all():
      total += item.qty * item.unit_price
      for add_on in item.itemaddon_set.all():
        total += add_on.qty * add_on.unit_price
    
    return round(total, 0)
  
admin.site.register(Item)
admin.site.register(Status)
admin.site.register(Customer)
admin.site.register(ItemAddOn)