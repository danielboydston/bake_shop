# Generated by Django 4.2.7 on 2023-12-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0005_outputpackaging'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outputpackaging',
            name='active',
        ),
        migrations.AddField(
            model_name='outputpackaging',
            name='unit_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
