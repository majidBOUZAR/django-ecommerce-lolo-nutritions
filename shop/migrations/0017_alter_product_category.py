# Generated by Django 4.0.3 on 2022-06-14 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_product_quantity1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FL', 'Farine_Semoul'), ('P', 'Pates'), ('G', 'Gateaux'), ('S', 'Sucrerie'), ('OF', 'Graines'), ('L', 'Laitiers'), ('B', 'Boisson'), ('PFM', 'Produit_Fait_Maison'), ('E', 'Epices'), ('CM', 'Compliment Alimentaire'), ('PGP', 'Produit_Gateaux_Patisserie')], max_length=3),
        ),
    ]
