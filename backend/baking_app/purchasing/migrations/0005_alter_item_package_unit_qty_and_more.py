# Generated by Django 4.2.7 on 2023-12-02 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchasing', '0004_alter_purchaseorder_shipping_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='package_unit_qty',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='purchase_qty',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
