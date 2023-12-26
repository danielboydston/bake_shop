from django.db import models
from units.models import HasPhysicalQty

class Output(HasPhysicalQty):
    output_date = models.DateTimeField()
    product_variation = models.ForeignKey("catelog.Variation", on_delete=models.RESTRICT)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    class Meta:
        ordering = ("-output_date",)

    def __str__(self):
        return f"{self.output_date} {self.product_variation} {self.unit_cost}"
    
    def save(self, *args, **kwargs):
        self.unit_cost = self.product_variation.unit_cost()
        super(Output, self).save(*args, **kwargs)

    def add_on_cost(self):
        cost = 0
        for add_on in self.outputaddon_set.all():
            cost += add_on.qty * add_on.unit_cost
        return cost

    def packaging_cost(self):
        cost = 0
        for packaging in self.outputpackaging_set.all():
            cost += packaging.qty * packaging.unit_cost
        return cost

    def total_cost(self):
        return self.unit_cost * self.qty + self.add_on_cost() + self.packaging_cost()

class OutputAddOn(HasPhysicalQty):
    output = models.ForeignKey(Output, on_delete=models.CASCADE)
    ingredient = models.ForeignKey("recipes.Ingredient", on_delete=models.RESTRICT)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return f"{self.qty} {self.unit} {self.ingredient}"
    
    def save(self, *args, **kwargs):
        self.unit_cost = self.ingredient.cost_per_unit / self.ingredient.physical_qty.convert(self.unit, self.ingredient).qty
        super(OutputAddOn, self).save(*args, **kwargs)


class OutputPackaging(HasPhysicalQty):
    output = models.ForeignKey(Output, on_delete=models.CASCADE)
    ingredient = models.ForeignKey("recipes.Ingredient", on_delete=models.CASCADE)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    
    def __str__(self):
        return f"{self.qty} {self.unit} {self.ingredient}"
    
    def save(self, *args, **kwargs):
        self.unit_cost = self.ingredient.cost_per_unit / self.ingredient.physical_qty.convert(self.unit, self.ingredient).qty
        super(OutputPackaging, self).save(*args, **kwargs)
    