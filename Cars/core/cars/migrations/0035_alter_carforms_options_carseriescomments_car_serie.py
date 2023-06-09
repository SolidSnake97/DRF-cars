# Generated by Django 4.1.7 on 2023-03-16 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0034_rename_carfroms_carforms'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carforms',
            options={'verbose_name': 'form', 'verbose_name_plural': 'Car Forms'},
        ),
        migrations.AddField(
            model_name='carseriescomments',
            name='car_serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serie_of_car', to='cars.carseries'),
        ),
    ]
