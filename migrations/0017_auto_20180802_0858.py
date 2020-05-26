# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 12:58
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poyosei', '0016_auto_20180802_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalplanteur',
            name='production_commerciale_totale',
        ),
        migrations.RemoveField(
            model_name='planteur',
            name='production_commerciale_totale',
        ),
        migrations.AlterField(
            model_name='historicalplanteur',
            name='référence_individuelle_définitive',
            field=models.DecimalField(blank=True, decimal_places=0, default=Decimal('0'), max_digits=100, verbose_name='Référence individuelle définitive'),
        ),
        migrations.AlterField(
            model_name='planteur',
            name='référence_individuelle_définitive',
            field=models.DecimalField(blank=True, decimal_places=0, default=Decimal('0'), max_digits=100, verbose_name='Référence individuelle définitive'),
        ),
    ]
