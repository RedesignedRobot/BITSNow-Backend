# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-01 05:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='eEndDate',
        ),
        migrations.RemoveField(
            model_name='items',
            name='eStartDate',
        ),
    ]
