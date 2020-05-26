# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 12:51
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poyosei', '0015_auto_20180611_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalplanteur',
            old_name='contremarque',
            new_name='contre_marque',
        ),
        migrations.RenameField(
            model_name='planteur',
            old_name='contremarque',
            new_name='contre_marque',
        ),
        migrations.AddField(
            model_name='historicalplanteur',
            name='production_commerciale_totale',
            field=models.DecimalField(decimal_places=0, default=Decimal('0.0'), max_digits=9),
        ),
        migrations.AddField(
            model_name='historicalplanteur',
            name='référence_individuelle_définitive',
            field=models.DecimalField(blank=True, decimal_places=0, default=Decimal('0'), max_digits=100, verbose_name='Référence individuelle défintive'),
        ),
        migrations.AddField(
            model_name='planteur',
            name='production_commerciale_totale',
            field=models.DecimalField(decimal_places=0, default=Decimal('0.0'), max_digits=9),
        ),
        migrations.AddField(
            model_name='planteur',
            name='référence_individuelle_définitive',
            field=models.DecimalField(blank=True, decimal_places=0, default=Decimal('0'), max_digits=100, verbose_name='Référence individuelle défintive'),
        ),
    ]
