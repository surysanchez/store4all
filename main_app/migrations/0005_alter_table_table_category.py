# Generated by Django 4.2 on 2023-05-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_itemphoto_item_remove_tablephoto_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_category',
            field=models.CharField(choices=[('miscellaneous', 'Miscellaneous'), ('wearables', 'Wearables'), ('consumables', 'Consumables'), ('homeables', 'Homeables'), ('gardenables', 'Gardenables'), ('entertainables', 'Entertainables')], default='miscellaneous'),
        ),
    ]
