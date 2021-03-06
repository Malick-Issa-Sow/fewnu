# Generated by Django 3.0.5 on 2021-02-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=100, verbose_name='Nom client')),
                ('id_client', models.IntegerField(blank=True, default=0, verbose_name="l'identifiant du client")),
                ('id_pret', models.IntegerField(blank=True, default=0, verbose_name="l'identifiant de mes prets")),
                ('article', models.TextField(blank=True, verbose_name="l'article du prets")),
                ('montant', models.IntegerField(blank=True, default=0, verbose_name='montant du pret')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Créé de compte cliet')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Mis à jour  du compte du pret')),
            ],
        ),
    ]
