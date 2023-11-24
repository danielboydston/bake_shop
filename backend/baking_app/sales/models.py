from django.db import models
from catelog.models import Variation
from units.models import Unit
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
    
    def __str__(self):
        return f"{self.order_date}"


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_variation = models.ForeignKey(Variation, on_delete=models.RESTRICT)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT, related_name="order_item")
    qty = models.DecimalField(max_digits=8, decimal_places=2)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.qty} {self.product_variation} {self.unit_price} {self.qty * self.unit_price}"
