# Generated by Django 3.2.6 on 2021-09-06 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_slider_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='Category',
            new_name='category',
        ),
    ]
