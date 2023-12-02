from django.db import models
from units.models import Unit, PhysicalQty
from catelog.models import Variation

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
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    baking_temp = models.IntegerField(null=True, blank=True)
    temp_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT, null=True, blank=True, related_name="temp_unit")
    baking_minutes_min = models.IntegerField(null=True, blank=True)
    baking_minutes_max = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    qty_numerator = models.IntegerField()
    qty_denominator = models.IntegerField(default=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.physical_qty = PhysicalQty(self.qty_numerator / self.qty_denominator, self.unit)

    def __str__(self):
        qty = f"{self.qty_numerator}"
        if self.qty_denominator > 1:
            qty = f"{qty}/{self.qty_denominator}"
        return f"{qty} {self.unit} {self.ingredient}"

class RecipeInstruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    disp_order = models.IntegerField()
    instruction = models.TextField()

    def __str__(self):
        return f"{self.disp_order}.  {self.instruction}"

class UnitCategoryConversion(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    unit_from = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="unit_from")
    unit_to = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="unit_to")
    formula = models.TextField()

    def __str__(self):
        return f"{self.ingredient}: {self.unit_from} to {self.unit_to}"

class ProductRecipe(models.Model):
    product_variation = models.ForeignKey(Variation, on_delete=models.RESTRICT)
    recipe = models.ForeignKey(Recipe, on_delete=models.RESTRICT)
    recipe_number = models.IntegerField()
    make_qty = models.IntegerField(default=1)
    make_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.product_variation}"