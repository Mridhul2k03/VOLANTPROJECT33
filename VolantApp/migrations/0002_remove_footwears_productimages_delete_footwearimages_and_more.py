# Generated by Django 5.0.6 on 2024-06-14 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolantApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footwears',
            name='productimages',
        ),
        migrations.DeleteModel(
            name='Footwearimages',
        ),
        migrations.DeleteModel(
            name='Footwears',
        ),
    ]