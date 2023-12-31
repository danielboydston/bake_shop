# Generated by Django 4.2.7 on 2023-12-24 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_productrecipe_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='ingredientcategory',
            options={'ordering': ('name',), 'verbose_name_plural': 'Ingredient categories'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'ordering': ('recipe', 'ingredient')},
        ),
        migrations.AlterModelOptions(
            name='recipeinstruction',
            options={'ordering': ('recipe', 'disp_order')},
        ),
    ]
