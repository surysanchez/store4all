# Generated by Django 4.2 on 2023-05-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_table_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(blank=True, upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='table',
            name='image',
            field=models.FileField(blank=True, upload_to='table_images/'),
        ),
    ]
