# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-09-05 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='streak',
            name='ip_address',
            field=models.GenericIPAddressField(default='192.168.1.1'),
            preserve_default=False,
        ),
    ]
