# Generated by Django 3.2.6 on 2021-09-27 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0003_auto_20210925_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('gener', models.CharField(blank=True, max_length=100, null=True)),
                ('rate', models.CharField(blank=True, max_length=5, null=True)),
                ('time', models.CharField(blank=True, max_length=10, null=True)),
                ('Directors', models.CharField(blank=True, max_length=200, null=True)),
                ('Actors', models.CharField(blank=True, max_length=300, null=True)),
                ('overview', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('Iframemovie', models.URLField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Movie.category')),
                ('contry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Movie.contry')),
                ('quality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Movie.quality')),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Movie.year')),
            ],
        ),
    ]
