# Generated by Django 4.2.7 on 2023-12-02 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_rename_produce_output_remove_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='unit_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]