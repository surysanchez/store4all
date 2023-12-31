# Generated by Django 4.2 on 2023-05-02 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0010_alter_table_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
        migrations.CreateModel(
            name='Cart_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.IntegerField(max_length=100)),
                ('item_description', models.TextField(default='', max_length=1024)),
                ('category', models.CharField(choices=[('miscellaneous', 'Miscellaneous'), ('wearables', 'Wearables'), ('consumables', 'Consumables'), ('homeables', 'Homeables'), ('gardenables', 'Gardenables'), ('entertainmentables', 'Entertainables')], default='miscellaneous')),
                ('image', models.FileField(blank=True, upload_to='item_images/')),
                ('Cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.cart')),
            ],
        ),
    ]
