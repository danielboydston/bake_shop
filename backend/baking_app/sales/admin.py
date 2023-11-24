from django.contrib import admin
from .models import Order, Item, Status, Customer

admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Status)
admin.site.register(Customer)