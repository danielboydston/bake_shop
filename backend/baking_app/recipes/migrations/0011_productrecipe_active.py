# Generated by Django 4.2.7 on 2023-12-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_rename_price_per_unit_ingredient_cost_per_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrecipe',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
