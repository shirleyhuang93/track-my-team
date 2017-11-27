# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20171126_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.FileField(default='default.png', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='avatar',
            field=models.FileField(default='default.png', upload_to='media/'),
        ),
    ]