# Generated by Django 3.2.6 on 2021-09-25 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tvseries',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
