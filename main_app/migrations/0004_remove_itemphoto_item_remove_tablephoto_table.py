# Generated by Django 4.2 on 2023-04-30 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemphoto',
            name='item',
        ),
        migrations.RemoveField(
            model_name='tablephoto',
            name='table',
        ),
    ]
