# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='country',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='team',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='team',
            name='city',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
