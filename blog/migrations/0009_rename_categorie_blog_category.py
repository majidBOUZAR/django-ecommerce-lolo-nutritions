# Generated by Django 4.0.3 on 2022-05-31 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='categorie',
            new_name='category',
        ),
    ]
