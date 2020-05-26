# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-31 13:56
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campagne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pacage', models.CharField(max_length=9)),
                ('annee', models.CharField(max_length=4)),
                ('RIT', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=9)),
                ('RID', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=9)),
                ('production_commerciale_totale', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=9)),
                ('commentaire', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Planteur',
            fields=[
                ('pacage', models.CharField(help_text='Un nombre de 9 chiffres', max_length=9, primary_key=True, serialize=False, verbose_name='Numéro pacage')),
                ('civilite', models.CharField(blank=True, choices=[('Mr', 'Monsieur'), ('gérant', 'Mr le gérant'), ('gérante', 'Mme la gérante'), ('Mme', 'Madame'), ('Societe', 'Societe'), ('Autre', 'Autre'), ('', '')], default='', max_length=20, verbose_name='Civilité')),
                ('nom', models.CharField(help_text='200 caractères maximum.', max_length=200, verbose_name='Nom')),
                ('prenom', models.CharField(help_text='200 caractères maximum.', max_length=100, verbose_name='Prénom')),
                ('siret', models.CharField(blank=True, help_text="code Insee permettant l'identification d'un établissement ou d'une entreprise française.", max_length=14, null=True, verbose_name='SIRET')),
                ('LPG', models.CharField(blank=True, help_text='Identifiant LPG du planteur.', max_length=100, null=True, verbose_name='Numéro LPG')),
                ('contremarque', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contremarque')),
                ('denomination', models.TextField(blank=True, help_text="Texte d'aide", max_length=100, null=True, verbose_name='Dénomination')),
                ('gerant', models.TextField(blank=True, help_text="Texte d'aide", null=True, verbose_name='Gérant')),
                ('adresse', models.CharField(blank=True, help_text='Adresse du planteur', max_length=255, null=True, verbose_name='Adresse')),
                ('adresse_complementaire', models.CharField(blank=True, max_length=255, null=True)),
                ('code_postal', models.CharField(blank=True, help_text='Code postal planteur', max_length=10, null=True, verbose_name='Code postal')),
                ('commune', models.CharField(blank=True, help_text='Commune du planteur', max_length=100, null=True, verbose_name='Commune')),
                ('telephone_principale', models.CharField(blank=True, help_text='Téléphone de contact', max_length=50, null=True, verbose_name='Numéro de téléphone')),
                ('telephone_secondaire', models.CharField(blank=True, help_text='téléphone de contact', max_length=50, null=True, verbose_name='Autre téléphone')),
                ('courriel', models.EmailField(blank=True, help_text='Adresse de courriel de contact.', max_length=254, null=True, verbose_name='Courriel')),
                ('dateNaissance', models.DateField(blank=True, help_text='Date de naissance du planteur', null=True, verbose_name='Date de naissance')),
                ('date_adhesion', models.DateField(blank=True, help_text='Date adhésion', null=True, verbose_name="Date d'adhésion à l'organisme de production")),
                ('numero_exemption_Diecte', models.CharField(blank=True, help_text="Numéro d'exemption DIECTE", max_length=50, null=True, verbose_name="Numéro d'exemption DIECTE")),
                ('date_fin_Diecte', models.DateField(blank=True, help_text="Date de fin d'exemption DIECTE", null=True, verbose_name="Date de fin d'exemption DIECTE")),
                ('entreprise_associé', models.TextField(blank=True, help_text='Autre entreprise associé', null=True, verbose_name='Entreprise associé par Actionnaire')),
                ('controle', models.BooleanField(default=False, help_text='Le planteur est-il exempte de contrôle ?', verbose_name='Exemption de contrôle')),
                ('date_cessation_Activite', models.DateField(blank=True, help_text="Date de cessation d'activité", null=True, verbose_name="Date de cessation d'activité")),
                ('commentaire', models.TextField(blank=True, help_text="Toute information utile à l'instruction", null=True, verbose_name='Commentaire')),
                ('date_creation', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='campagne',
            unique_together=set([('pacage', 'annee')]),
        ),
    ]
