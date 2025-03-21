# Generated by Django 5.1.4 on 2025-03-18 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('deliveries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_date', models.DateField()),
                ('zip_code', models.CharField(max_length=8)),
                ('number', models.CharField(max_length=5)),
                ('height', models.FloatField()),
                ('depth', models.FloatField()),
                ('width', models.FloatField()),
                ('wieght', models.FloatField()),
                ('estimated_price', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dr_customer', to='customers.customer')),
            ],
        ),
    ]
