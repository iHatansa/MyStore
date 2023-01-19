# Generated by Django 4.1.4 on 2023-01-19 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0048_merge_20230119_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Admin',
        ),
        migrations.AddField(
            model_name='cart',
            name='Admins',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.admins'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admins',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]