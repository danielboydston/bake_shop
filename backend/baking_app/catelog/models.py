from django.db import models
from units.models import Unit
from decimal import Decimal
from recipes.models import PhysicalQty

class Category(models.Model):
    name = models.CharField(max_length=255)
    disp_order = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        if self.name is not None:
            display_name = f"{self.product} {self.name}"
        else:
            display_name = self.product
        return display_name
    
    def unit_cost(self):
        """
        The unit cost of the product, derived from the active recipe cost and the make qty/unit
        """

        total_cost = Decimal(0)
        # Get the active productrecipe
        product_recipes = self.productrecipe_set.filter(active=True)
        for pr in product_recipes:
            print(f"{pr.recipe} - ${pr.recipe.cost()}")
            total_cost += pr.recipe.cost() / pr.make_qty 
        
        # Total up the cost of packaging
        packaging = self.variationpackaging_set.filter(active=True)
        for pack in packaging:
            pq = pack.physical_qty.convert(pack.ingredient.base_unit, pack.ingredient)
            total_cost += pq.qty * pack.ingredient.cost_per_unit
            
        return total_cost


class VariationPackaging(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    ingredient = models.ForeignKey("recipes.Ingredient", on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    active = models.BooleanField(default=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.unit:
            self.physical_qty = PhysicalQty(self.qty, self.unit)

    def __str__(self):
        return f"{self.qty} {self.unit} {self.ingredient}"
    

class VariationAddOn(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    ingredient = models.ForeignKey("recipes.Ingredient", on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    active = models.BooleanField(default=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.unit:
            self.physical_qty = PhysicalQty(self.qty, self.unit)

    def __str__(self):
        return f"{self.qty} {self.unit} {self.ingredient}"
