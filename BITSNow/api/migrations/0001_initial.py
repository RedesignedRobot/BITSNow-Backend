# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-13 20:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eTitle', models.CharField(default='', max_length=255)),
                ('eDesc', models.CharField(default='', max_length=255)),
                ('cName', models.CharField(default='', max_length=255)),
                ('cId', models.CharField(default='', max_length=255)),
                ('eStartDate', models.DateTimeField(blank=True, default=datetime.datetime(2017, 10, 13, 20, 43, 5, 847644))),
                ('eEndDate', models.DateTimeField(blank=True, default=datetime.datetime(2017, 10, 13, 20, 43, 5, 847667))),
            ],
        ),
    ]
