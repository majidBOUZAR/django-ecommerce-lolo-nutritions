# Generated by Django 4.0.3 on 2022-06-01 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
