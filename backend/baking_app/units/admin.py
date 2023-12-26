from django.contrib import admin

from .models import Unit, UnitCategory, BaseUnit


admin.site.register(UnitCategory)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
  list_display = ("name", "abbr", "category", "unit_system")

@admin.register(BaseUnit)
class BaseUnitAdmin(admin.ModelAdmin):
  list_display = ("category", "unit")

