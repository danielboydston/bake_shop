from django.contrib import admin
from .models import Order, Item, Status, Customer, ItemAddOn

admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Status)
admin.site.register(Customer)
admin.site.register(ItemAddOn)