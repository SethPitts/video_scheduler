# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_scheduler', '0002_auto_20171030_0319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='id',
        ),
        migrations.AlterField(
            model_name='video',
            name='video_title',
            field=models.TextField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
