from django.contrib import admin
from config.models import Config
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from .models import Recipe, Ingredient, RecipeIngredient, RecipeInstruction, UnitCategoryConversion, IngredientCategory, ProductRecipe

currency_symbol = Config.objects.get(item="currency_symbol").value
currency_decimals = int(Config.objects.get(item="currency_decimals").value)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
  list_display = ("name", "ingredients", "instructions")

  def ingredients(self, obj: Recipe):
    count = obj.recipeingredient_set.count()
    url = f"{reverse("admin:recipes_recipeingredient_changelist")}?{urlencode({"recipe__id": f"{obj.id}"})}"
    return format_html('<a href="{}">{} Ingredients</a>', url, count)
  
  def instructions(self, obj: Recipe):
    count = obj.recipeinstruction_set.count()
    url = f"{reverse("admin:recipes_recipeinstruction_changelist")}?{urlencode({"recipe__id": f"{obj.id}"})}"
    return format_html('<a href="{}">{} Instructions</a>', url, count)
  

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
  list_display = ("name", "category", "base_unit", "cost_per_unit_display")
  list_filter = ("category",)
  search_fields = ("name__contains", )

  def cost_per_unit_display(self, obj):
    return f"{currency_symbol}{round(obj.cost_per_unit, currency_decimals)}"


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
  list_display = ("edit", "recipe_link", "qty", "unit", "ingredient")
  list_filter = ("recipe",)

  def edit(self, obj):
    return "Edit"
  
  def recipe_link(self, obj: RecipeIngredient):
    url = f"{reverse("admin:recipes_recipe_changelist")}?{urlencode({"recipe__id": f"{obj.recipe.id}"})}"
    return format_html('<a href="{}">{}</a>', url, f"{obj.recipe}")
  
  recipe_link.short_description = "recipe"

@admin.register(RecipeInstruction)
class RecipeInstruction(admin.ModelAdmin):
  list_display = ("recipe", "disp_order", "instruction")
  list_filter = ("recipe",)

admin.site.register(UnitCategoryConversion)
admin.site.register(IngredientCategory)


@admin.register(ProductRecipe)
class ProductRecipeAdmin(admin.ModelAdmin):
  list_display = ("product_variation", "recipe", "active")
  list_filter = ("product_variation", "active")