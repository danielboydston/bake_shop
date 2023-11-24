# Generated by Django 4.2.7 on 2023-11-24 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0003_unit_data'),
        ('catelog', '0001_initial'),
        ('recipes', '0002_alter_recipe_baking_minutes_max_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='product_variation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catelog.variation'),
        ),
        migrations.CreateModel(
            name='ProductRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_number', models.IntegerField()),
                ('make_qty', models.IntegerField(default=1)),
                ('notes', models.TextField(blank=True, null=True)),
                ('make_unit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='units.unit')),
                ('product_variation', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catelog.variation')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='recipes.recipe')),
            ],
        ),
    ]
