from django.contrib import admin
from .models import Output, OutputAddOn, OutputPackaging
from config.models import Config

currency_decimals = int(Config.objects.get(item="currency_decimals").value)
currency_symbol = Config.objects.get(item="currency_symbol").value

@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
  list_display = ("output_date", "product_variation", "qty", "unit", "cost", "add_on_cost", "packaging_cost", "total_cost")
  list_filter = ("output_date",)

  def cost(self, obj):
    return f"{currency_symbol} {round(obj.product_variation.unit_cost() * obj.qty, currency_decimals):.2f}"
  
  def add_on_cost(self, obj:Output):
    return f"{currency_symbol} {round(obj.add_on_cost(), currency_decimals)}"
  
  def packaging_cost(self, obj:Output):
    return f"{currency_symbol} {round(obj.packaging_cost(), currency_decimals)}"

  def total_cost(self, obj:Output):
    return f"{currency_symbol} {round(obj.total_cost(), currency_decimals)}"
  

@admin.register(OutputAddOn)
class OutputAddOnAdmin(admin.ModelAdmin):
  list_display = ("output", "ingredient", "qty", "unit")
  list_filter = ("output",)


@admin.register(OutputPackaging)
class OutputPackagingAdmin(admin.ModelAdmin):
  list_display = ("output", "ingredient", "qty", "unit")
  list_filter = ("output",)