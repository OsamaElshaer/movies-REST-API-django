# Generated by Django 3.2.6 on 2021-09-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20210908_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='imageposter',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
