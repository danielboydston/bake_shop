# Generated by Django 4.2.7 on 2023-12-17 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0006_modify_formula_placeholder'),
        ('recipes', '0011_productrecipe_active'),
        ('production', '0003_alter_output_unit_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutputAddOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=4, max_digits=10)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='recipes.ingredient')),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.output')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='units.unit')),
            ],
        ),
    ]
