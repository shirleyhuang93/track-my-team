# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20171126_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='player',
            name='uin',
            field=models.IntegerField(blank=True, null=True, verbose_name='UIN'),
        ),
        migrations.AlterField(
            model_name='player',
            name='usau_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='USAU ID'),
        ),
    ]
