# Generated by Django 4.0.3 on 2022-06-03 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_customer_order_item_alter_product_quantity1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='order_item',
        ),
    ]
