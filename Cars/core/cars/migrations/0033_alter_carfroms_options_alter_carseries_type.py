# Generated by Django 4.1.7 on 2023-03-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0032_carfroms_remove_carseries_type_carseries_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carfroms',
            options={'verbose_name': 'form', 'verbose_name_plural': 'forms'},
        ),
        migrations.AlterField(
            model_name='carseries',
            name='type',
            field=models.ManyToManyField(null=True, related_name='formalar', to='cars.carfroms'),
        ),
    ]
