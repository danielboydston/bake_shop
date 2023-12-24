from django.contrib import admin
from .models import Output, OutputAddOn


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
  list_display = ("output_date", "product_variation", "qty", "unit", "cost", "add_on_cost", "total_cost")
  list_filter = ("output_date",)

  def cost(self, obj):
    return round(obj.product_variation.unit_cost() * obj.qty, 0)
  
  def add_on_cost(self, obj:Output):
    cost = 0
    for add_on in obj.outputaddon_set.all():
      cost += add_on.qty * add_on.unit_cost
    return round(cost, 0)

  def total_cost(self, obj:Output):
    return round(self.cost(obj) + self.add_on_cost(obj), 0)

admin.site.register(OutputAddOn)