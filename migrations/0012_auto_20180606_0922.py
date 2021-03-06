# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-06 13:22
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poyosei', '0011_auto_20180606_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='mouvement',
            name='quantite_reference_individuelle_accorde2',
            field=models.DecimalField(blank=True, decimal_places=0, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='mouvement',
            name='pacage_cedant',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mouvement',
            name='pacage_repreneur',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mouvement',
            name='type_reference_individuelle_modifie',
            field=models.CharField(blank=True, choices=[('définitive', 'définitive'), ('temporaire', 'temporaire'), ('autre', 'autre'), ('', '')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='typemouvementmodel',
            name='type_mouvement',
            field=models.CharField(choices=[("transfert total d'une exploitation", "transfert total d'une exploitation"), ('Transfert de Référence Individuelle avec cession partielle de foncier', 'Transfert de Référence Individuelle avec cession partielle de foncier'), ('Transfert de Référence Individuelle sans foncier', 'Transfert de Référence Individuelle sans foncier'), ('Reprise administrative', 'Reprise administrative'), ('Cession volontaire définitive', 'Cession volontaire définitive'), ('Cession volontaire temporaire', 'Cession volontaire temporaire'), ('Cessation d’activite sans repreneur', 'Cessation d’activite sans repreneur'), ('Attribution de Reference Individuelle par la reserve', 'Attribution de Reference Individuelle par la réserve'), ('Autre', 'Autre'), ('', '')], default='', max_length=100),
        ),
    ]
