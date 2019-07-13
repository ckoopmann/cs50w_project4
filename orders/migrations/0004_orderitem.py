# Generated by Django 2.0.3 on 2019-07-13 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MenuItem')),
                ('toppings', models.ManyToManyField(to='orders.Topping')),
            ],
        ),
    ]
