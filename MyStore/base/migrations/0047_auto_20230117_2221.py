# Generated by Django 3.0.14 on 2023-01-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Admin',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Product',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cart',
            name='User',
            field=models.CharField(max_length=15),
        ),
    ]
