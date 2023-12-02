# Generated by Django 4.2.7 on 2023-12-02 13:19

from django.db import migrations
from units.models import Unit
from recipes.models import UnitCategoryConversion

def modify_data(apps, schema_editor):
    units = Unit.objects.all()
    for unit in units:
        unit.conversion_from_base = unit.conversion_from_base.replace('b','q')
        unit.conversion_to_base = unit.conversion_to_base.replace('u','q')
        unit.save()

    uccs = UnitCategoryConversion.objects.all()
    for ucc in uccs:
        ucc.formula = ucc.formula.replace('u','q')
        ucc.save()

class Migration(migrations.Migration):

    dependencies = [
        ('units', '0005_alter_config_item'),
    ]

    operations = [
        migrations.RunPython(modify_data)
    ]
