# Generated by Django 3.2.6 on 2021-09-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_slider_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]