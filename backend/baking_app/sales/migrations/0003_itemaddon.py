# Generated by Django 4.2.7 on 2023-12-17 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0006_modify_formula_placeholder'),
        ('recipes', '0011_productrecipe_active'),
        ('sales', '0002_alter_item_qty_alter_item_unit_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAddOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=4, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='recipes.ingredient')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.item')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='units.unit')),
            ],
        ),
    ]
