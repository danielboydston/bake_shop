from django.contrib import admin
from .models import Vendor, StatusCategory, Status, PurchaseOrder, Item

# Register your models here.

admin.site.register(Vendor)
admin.site.register(StatusCategory)
admin.site.register(Status)
admin.site.register(PurchaseOrder)
admin.site.register(Item)
