# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poyosei', '0048_auto_20180820_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmouvement',
            name='type_mouvement',
            field=models.CharField(choices=[("transfert total d'une exploitation", "transfert total d'une exploitation"), ('Transfert de référence rndividuelle avec cession partielle de foncier', 'Transfert de référence individuelle avec cession partielle de foncier'), ('Transfert de Référence Individuelle sans foncier', 'Transfert de Référence Individuelle sans foncier'), ('Reprise administrative', 'Reprise administrative'), ('Cession volontaire définitive', 'Cession volontaire définitive'), ('Cession volontaire temporaire', 'Cession volontaire temporaire'), ('Cessation d’activite sans repreneur', 'Cessation d’activite sans repreneur'), ('Attribution de Reference Individuelle par la reserve', 'Attribution de Reference Individuelle par la réserve'), ('Autre', 'Autre'), ('', '')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='typemouvementmodel',
            name='type_mouvement',
            field=models.CharField(choices=[("transfert total d'une exploitation", "transfert total d'une exploitation"), ('Transfert de référence rndividuelle avec cession partielle de foncier', 'Transfert de référence individuelle avec cession partielle de foncier'), ('Transfert de Référence Individuelle sans foncier', 'Transfert de Référence Individuelle sans foncier'), ('Reprise administrative', 'Reprise administrative'), ('Cession volontaire définitive', 'Cession volontaire définitive'), ('Cession volontaire temporaire', 'Cession volontaire temporaire'), ('Cessation d’activite sans repreneur', 'Cessation d’activite sans repreneur'), ('Attribution de Reference Individuelle par la reserve', 'Attribution de Reference Individuelle par la réserve'), ('Autre', 'Autre'), ('', '')], default='', max_length=100),
        ),
    ]
