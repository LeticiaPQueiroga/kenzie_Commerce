# Generated by Django 4.2.2 on 2023-07-03 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_users_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isAvailable',
            field=models.BooleanField(default=True),
        ),
    ]
