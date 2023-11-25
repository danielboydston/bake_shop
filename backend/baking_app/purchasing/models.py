from django.db import models
from recipes.models import Ingredient
from units.models import Unit

class StatusCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:  
        verbose_name_plural = 'Status categories'

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(StatusCategory, on_delete=models.RESTRICT)
    sequence = models.IntegerField()

    class Meta:  
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateField()
    status_id = models.ForeignKey(Status, on_delete=models.RESTRICT)
    shipping_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.order_date} {self.vendor_id} {self.status_id}"

class Item(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    package_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT, related_name="po_item")
    package_unit_qty = models.DecimalField(max_digits=8, decimal_places=2)
    purchase_qty = models.DecimalField(max_digits=8, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.purchase_qty} {self.ingredient} {self.package_unit_qty} {self.package_unit} {self.status}"

