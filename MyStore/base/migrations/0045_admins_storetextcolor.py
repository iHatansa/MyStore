# Generated by Django 3.0.14 on 2023-01-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_auto_20230116_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='admins',
            name='StoreTextColor',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
