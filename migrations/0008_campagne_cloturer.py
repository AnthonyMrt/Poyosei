# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-01 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poyosei', '0007_auto_20180531_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='campagne',
            name='cloturer',
            field=models.BooleanField(default=False),
        ),
    ]
