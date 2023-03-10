# Generated by Django 3.0.14 on 2023-01-29 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0066_auto_20230129_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AlterField(
            model_name='completedorder',
            name='Order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Order'),
        ),
    ]
