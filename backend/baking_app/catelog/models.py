from django.db import models

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

        # Get the active productrecipe
        product_recipe = self.productrecipe_set.get(active=True)
        product_cost = product_recipe.recipe.cost() / product_recipe.make_qty 

        return product_cost