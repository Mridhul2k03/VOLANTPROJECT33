# Generated by Django 5.0.6 on 2024-06-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VolantApp', '0033_alter_ordermodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(choices=[('shipped', 'shipped'), ('order-placed', 'order-placed'), ('delivered', 'delivered'), ('cancelled', 'cancelled'), ('dispatched', 'dispatched')], default='order-placed', max_length=100),
        ),
    ]
