# Generated by Django 4.1.1 on 2022-10-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_orders_deliverystatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='currentLat',
            field=models.PositiveSmallIntegerField(verbose_name='Latitud'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='currentLng',
            field=models.PositiveSmallIntegerField(verbose_name='Longitud'),
        ),
    ]