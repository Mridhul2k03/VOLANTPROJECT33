# Generated by Django 5.0.6 on 2024-06-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VolantApp', '0035_alter_ordermodel_status_usercontactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='status',
            field=models.CharField(choices=[('sended', 'sended'), ('seened', 'seened')], default='sended', max_length=100),
        ),
        migrations.AddField(
            model_name='usercontactmodel',
            name='status',
            field=models.CharField(choices=[('sended', 'sended'), ('seened', 'seened')], default='sended', max_length=100),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(choices=[('order-placed', 'order-placed'), ('shipped', 'shipped'), ('cancelled', 'cancelled'), ('dispatched', 'dispatched'), ('delivered', 'delivered')], default='order-placed', max_length=100),
        ),
    ]
