# Generated by Django 3.2.6 on 2021-09-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_tvseries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
