# Generated by Django 2.0.3 on 2019-07-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20190714_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='extras',
            field=models.ManyToManyField(to='orders.Extra'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='toppings',
            field=models.ManyToManyField(to='orders.Topping'),
        ),
    ]
