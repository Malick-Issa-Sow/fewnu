# Generated by Django 3.0.5 on 2021-02-23 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boutique',
            name='nom_gerant',
        ),
    ]
