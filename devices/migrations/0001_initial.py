# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-09-05 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('checkin_identifier', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
    ]
