# Generated by Django 4.1.1 on 2022-10-20 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driversId', models.PositiveSmallIntegerField(verbose_name='id del conductor')),
                ('currentLat', models.CharField(max_length=200, verbose_name='Latitud')),
                ('currentLng', models.CharField(max_length=200, verbose_name='Longitud')),
                ('lastUpdate', models.DateTimeField(verbose_name='última actualización')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='driver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.driver', verbose_name='conductor'),
            preserve_default=False,
        ),
    ]