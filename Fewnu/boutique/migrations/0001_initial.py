# Generated by Django 3.0.5 on 2021-02-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boutique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_gerant', models.CharField(max_length=100, verbose_name='Nom gerant')),
                ('nom_boutique', models.CharField(max_length=100, verbose_name='Nom boutique')),
                ('id_mesboutique', models.IntegerField(blank=True, default=0, verbose_name="l'identifiant de mes boutiques")),
                ('adresse', models.TextField(blank=True, verbose_name="l'adresse de la boutiques")),
                ('id_boutique', models.IntegerField(blank=True, default=0, verbose_name="l'identifiant de la boutique")),
                ('telephone_boutique', models.IntegerField(blank=True, default=0, verbose_name='telephone_boutique')),
                ('email_boutique', models.EmailField(max_length=254, verbose_name='email boutique')),
                ('confirme_mots_passe', models.CharField(max_length=254, verbose_name='confirme le mots de passe de la boutique')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Créé de compte cliet')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Mis à jour  du compte du boutique')),
            ],
        ),
    ]
