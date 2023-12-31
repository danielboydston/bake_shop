from django.db import models
from catelog.models import Variation
from units.models import Unit, HasPhysicalQty
from baking_app.utils import phone_to_display

class Status(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Statuses"
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        display = ""
        if self.name is not None:
            display = self.name
        if self.phone is not None:
            if len(display) > 0:
                display = f"{display}, "
            display = f"{display}{phone_to_display(self.phone)}"
        if self.email is not None:
            if len(display) > 0:
                display = f"{display}, "
            display = f"{display}{self.email}"
        display.strip()
        if len(display) == 0:
            display = f"Customer {self.pk}"
        return display

class Order(models.Model):
    order_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)
    
    class Meta:
        ordering = ("-order_date",)

    def __str__(self):
        return f"{self.order_date} {self.customer}"
    
    def total_price(self):
        total = 0
        for item in self.item_set.all():
            total += item.qty * item.unit_price
            for add_on in item.itemaddon_set.all():
                total += add_on.qty * add_on.unit_price
        return total


class Item(HasPhysicalQty):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_variation = models.ForeignKey(Variation, on_delete=models.RESTRICT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.qty} {self.product_variation} {self.unit_price} {self.qty * self.unit_price}"


class ItemAddOn(HasPhysicalQty):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ingredient = models.ForeignKey("recipes.ingredient", on_delete=models.RESTRICT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.qty} {self.unit} {self.ingredient}"