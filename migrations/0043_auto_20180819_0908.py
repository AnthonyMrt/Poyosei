# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-19 13:08
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poyosei', '0042_ajoutmouvement'),
    ]

    operations = [
        migrations.AddField(
            model_name='campagne',
            name='ri_Total',
            field=models.DecimalField(decimal_places=0, default=Decimal('0.0'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='ajoutmouvement',
            name='informations',
            field=models.TextField(blank=True),
        ),
    ]