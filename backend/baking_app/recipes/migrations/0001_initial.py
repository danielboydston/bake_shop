# Generated by Django 4.2.7 on 2023-11-22 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('units', '__first__'),
        ('catelog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('base_unit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='units.unit')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Ingredient categories',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_number', models.IntegerField()),
                ('make_qty', models.IntegerField(default=1)),
                ('notes', models.TextField(blank=True, null=True)),
                ('baking_temp', models.IntegerField(null=True)),
                ('baking_minutes_min', models.IntegerField(null=True)),
                ('baking_minutes_max', models.IntegerField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('make_unit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='make_unit', to='units.unit')),
                ('product_variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catelog.variation')),
                ('temp_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='temp_unit', to='units.unit')),
            ],
        ),
        migrations.CreateModel(
            name='UnitCategoryConversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.TextField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='recipes.ingredient')),
                ('unit_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_from', to='units.unit')),
                ('unit_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_to', to='units.unit')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disp_order', models.IntegerField()),
                ('instruction', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_numerator', models.IntegerField()),
                ('qty_denominator', models.IntegerField(default=1)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='recipes.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='units.unit')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='recipes.ingredientcategory'),
        ),
    ]
