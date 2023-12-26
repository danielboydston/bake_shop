from django.db import models
from recipes.models import Ingredient
from units.models import Unit, PhysicalQty, HasPhysicalQty

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
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.order_date} {self.vendor} {self.status}"
    
    def item_cost(self):
        cost = 0
        for item in self.poitem_set.all():
            cost += item.purchase_price
        return cost

    def total_cost(self):
        return self.item_cost() + self.shipping_fee

class POItem(HasPhysicalQty):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    purchase_qty = models.DecimalField(max_digits=10, decimal_places=4)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.purchase_qty} {self.ingredient} {self.qty} {self.unit} {self.status}"
    
    def save(self, *args, **kwargs):
        self.physical_qty = PhysicalQty(self.qty, self.unit)
        super(POItem, self).save(*args, **kwargs)        
        # Update the ingredient cost per unit based on this purchase
        self.ingredient.cost_per_unit = self.purchase_price / self.purchase_qty / self.physical_qty.convert(self.ingredient.base_unit, self.ingredient).qty
        self.ingredient.save()
        
