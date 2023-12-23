from django.db import models
from units.models import Unit

class Output(models.Model):
    output_date = models.DateTimeField()
    product_variation = models.ForeignKey("catelog.Variation", on_delete=models.RESTRICT)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    qty = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.physical_qty = PhysicalQty(self.qty, self.unit)

    def __str__(self):
        return f"{self.output_date} {self.product_variation} {self.unit_cost}"
    

class OutputAddOn(models.Model):
    output = models.ForeignKey(Output, on_delete=models.CASCADE)
    ingredient = models.ForeignKey("recipes.Ingredient", on_delete=models.RESTRICT)
    qty = models.DecimalField(max_digits=10, decimal_places=4)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.qty} {self.unit} {self.ingredient}"
