# Generated by Django 3.2.6 on 2021-09-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_auto_20210925_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newrelease',
            name='Actors',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='newrelease',
            name='Iframemovie',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='newrelease',
            name='gener',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newrelease',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='slider',
            name='actors',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='quality',
            field=models.CharField(blank=True, choices=[('HD', 'HD'), ('HDRip', 'HDRip'), ('SD', 'SD'), ('TS', 'TS'), ('CAM', 'CAM')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='submovie',
            name='Actors',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='submovie',
            name='Directors',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='submovie',
            name='Iframemovie',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='submovie',
            name='gener',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='submovie',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='iframe',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]