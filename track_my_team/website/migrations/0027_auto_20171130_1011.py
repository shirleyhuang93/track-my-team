# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20171130_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=64),
        ),
    ]
