# Generated by Django 4.2.7 on 2023-12-01 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='item',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
