# Generated by Django 4.1.1 on 2022-10-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_driver_orders_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='driverName',
            field=models.CharField(default='Manuel', max_length=200, verbose_name='Nombre del conductor'),
            preserve_default=False,
        ),
    ]