# Generated by Django 4.0.3 on 2022-06-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity1',
            field=models.CharField(choices=[('sold', 'sold'), ('available', 'available')], default='available', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]