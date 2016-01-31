# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_auto_20160109_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='description',
            field=models.CharField(default='n/a', max_length=2500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calendar',
            name='name',
            field=models.CharField(default='n/a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeslot',
            name='free',
            field=models.BooleanField(default=True),
        ),
    ]