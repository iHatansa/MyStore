# Generated by Django 4.1.4 on 2023-02-06 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0074_delete_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='admins',
            name='StorePhone',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admins',
            name='storeEmail',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
