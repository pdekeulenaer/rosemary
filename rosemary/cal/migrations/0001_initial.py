# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=400)),
                ('party_size', models.IntegerField(default=1)),
                ('start', models.DateTimeField(verbose_name=b'starting time')),
                ('end', models.DateTimeField(verbose_name=b'ending time')),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='calendar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cal.Calendar'),
        ),
    ]
