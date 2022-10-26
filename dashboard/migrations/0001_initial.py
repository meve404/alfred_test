# Generated by Django 4.1.1 on 2022-10-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordersName', models.CharField(max_length=200, verbose_name='Nombre de la orden')),
                ('deliveryTime', models.DateTimeField(verbose_name='Tiempo de entrega')),
                ('pickUp', models.CharField(max_length=200, verbose_name='Recogida')),
                ('deliverTo', models.CharField(max_length=200, verbose_name='Destino')),
                ('deliveryStatus', models.CharField(max_length=200, verbose_name='Estado')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]