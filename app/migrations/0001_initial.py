# Generated by Django 4.0.3 on 2022-06-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('adress', models.CharField(max_length=100, null=True)),
                ('open_time', models.TimeField(blank=True, null=True)),
                ('close_time', models.TimeField(blank=True, null=True)),
                ('emaill', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/%d/%m/%y')),
                ('title', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]