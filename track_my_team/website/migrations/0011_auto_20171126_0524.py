# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20171126_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='avatar',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/default.png', null=True, upload_to='media/'),
        ),
    ]
