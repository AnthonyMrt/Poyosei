# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poyosei', '0043_auto_20180819_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reconstitutiontonnage',
            name='pacage',
            field=models.CharField(max_length=9),
        ),
    ]
