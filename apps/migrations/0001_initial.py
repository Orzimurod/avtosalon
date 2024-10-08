# Generated by Django 5.1 on 2024-08-22 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='brand_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='CarColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('car', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('produced_year', models.DateField()),
                ('price', models.PositiveIntegerField()),
                ('case', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('fuel', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='apps.carbrand')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='apps.carcolor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='apps.category')),
            ],
        ),
    ]
