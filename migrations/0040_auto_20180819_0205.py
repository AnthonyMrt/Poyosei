# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-19 06:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poyosei', '0039_auto_20180818_0144'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='newMouvement',
            new_name='ajoutMouvement',
        ),
        migrations.AlterUniqueTogether(
            name='reconstitutiontonnage',
            unique_together=set([('pacage', 'annee')]),
        ),
    ]
