from django.db import models
from units.models import Unit, PhysicalQty, UnitCategory
from catelog.models import Variation
from decimal import Decimal

class IngredientCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Ingredient categories"

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(IngredientCategory, on_delete=models.RESTRICT, default=1)
    base_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    baking_temp_degrees = models.IntegerField(null=True, blank=True)
    baking_temp_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT, null=True, blank=True, related_name="temp_unit")
    baking_minutes_min = models.IntegerField(null=True, blank=True)
    baking_minutes_max = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.baking_temp = PhysicalQty(self.baking_temp_degrees, self.baking_temp_unit)

    def __str__(self):
        return f"{self.name}"
    
    def cost(self) -> Decimal:
        """
        Total the cost of each recipe ingredient to calculate the recipe cost.
        """
        total_cost = Decimal(0)
        for ri in self.recipeingredient_set.all():
            # Convert the PhysicalQty to the ingredient base unit
            pq = ri.physical_qty.convert(ri.ingredient.base_unit, ri.ingredient)
            total_cost += pq.qty * ri.ingredient.cost_per_unit
            
        return Decimal(f"{total_cost:.2f}")

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    qty = models.DecimalField(max_digits=10, decimal_places=4)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # if self.unit:
        #     self.physical_qty = PhysicalQty(self.qty, self.unit)

    def __str__(self):
        return f"{self.qty} {self.unit} {self.ingredient}"
        return f"{self.physical_qty} {self.ingredient}"

class RecipeInstruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    disp_order = models.IntegerField()
    instruction = models.TextField()

    def __str__(self):
        return f"{self.disp_order}.  {self.instruction}"

class UnitCategoryConversion(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    formula = models.TextField()
    category_from = models.ForeignKey(UnitCategory, on_delete=models.RESTRICT, related_name="category_from")
    category_to = models.ForeignKey(UnitCategory, on_delete=models.RESTRICT, related_name="category_to")

    def __str__(self):
        return f"{self.ingredient}: {self.category_from} to {self.category_to}"

class ProductRecipe(models.Model):
    product_variation = models.ForeignKey(Variation, on_delete=models.RESTRICT)
    recipe = models.ForeignKey(Recipe, on_delete=models.RESTRICT)
    recipe_number = models.IntegerField()
    make_qty = models.IntegerField(default=1)
    make_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    notes = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_variation}"
    
    def activate(self):
        """
        Activates this recipe for the product variation.  Inactivates all other recipies for this product variation.
        """
        ProductRecipe.objects.filter(product_variation=self.product_variation).update(active=False)
        self.active = True
        self.save()
            