# Generated by Django 4.1.4 on 2023-02-11 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0076_remove_admins_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admins',
            name='StoreBackgroundColor',
        ),
    ]
