# Generated by Django 4.2 on 2023-04-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя покупателя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_name', models.CharField(max_length=50, verbose_name='Название детали')),
                ('last_name', models.CharField(max_length=50, verbose_name='Описание')),
                ('product', models.CharField(max_length=50, verbose_name='Изделие')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Название изделия')),
            ],
        ),
    ]
