from django.contrib import admin

from .models import Unit, UnitCategory, BaseUnit

admin.site.register(Unit)
admin.site.register(UnitCategory)
admin.site.register(BaseUnit)
