# Generated by Django 3.2.6 on 2021-09-06 19:41

import Home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newrelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('gener', models.CharField(blank=True, max_length=50, null=True)),
                ('quality', models.CharField(blank=True, max_length=10, null=True)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('contry', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.CharField(blank=True, max_length=10, null=True)),
                ('time', models.CharField(blank=True, max_length=10, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('Directors', models.CharField(blank=True, max_length=100, null=True)),
                ('Actors', models.CharField(blank=True, max_length=50, null=True)),
                ('overview', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('Iframemovie', models.URLField(blank=True, max_length=300, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('gener', models.CharField(blank=True, max_length=50, null=True)),
                ('quality', models.CharField(blank=True, max_length=10, null=True)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('contry', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.CharField(blank=True, max_length=10, null=True)),
                ('time', models.CharField(blank=True, max_length=10, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('Directors', models.CharField(blank=True, max_length=100, null=True)),
                ('Actors', models.CharField(blank=True, max_length=50, null=True)),
                ('overview', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('Iframemovie', models.URLField(blank=True, max_length=300, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=Home.models.images_trailer)),
                ('time', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('iframe', models.URLField()),
            ],
        ),
    ]
