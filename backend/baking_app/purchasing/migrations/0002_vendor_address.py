# Generated by Django 4.2.7 on 2023-11-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchasing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]