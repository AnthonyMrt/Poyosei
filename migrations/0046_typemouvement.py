# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poyosei', '0045_delete_ajoutmouvement'),
    ]

    operations = [
        migrations.CreateModel(
            name='typeMouvement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_mouvement', models.CharField(max_length=100)),
                ('informations', models.TextField(blank=True)),
            ],
        ),
    ]
