# Generated by Django 5.0.7 on 2024-08-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseoffer',
            name='amenities',
        ),
        migrations.AlterField(
            model_name='houseimages',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
