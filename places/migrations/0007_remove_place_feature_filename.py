# Generated by Django 4.0.3 on 2022-03-28 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_place_feature_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='feature_filename',
        ),
    ]
