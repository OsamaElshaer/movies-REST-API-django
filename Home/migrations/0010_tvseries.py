# Generated by Django 3.2.6 on 2021-09-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_auto_20210908_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tvseries',
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
    ]