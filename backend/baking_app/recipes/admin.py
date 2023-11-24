from django.contrib import admin

from .models import Recipe, Ingredient, RecipeIngredient, RecipeInstruction, UnitCategoryConversion, IngredientCategory, ProductRecipe
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeInstruction)
admin.site.register(UnitCategoryConversion)
admin.site.register(IngredientCategory)
admin.site.register(ProductRecipe)