# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-22 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0003_auto_20180521_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allianceraces',
            name='image',
        ),
        migrations.RemoveField(
            model_name='horderaces',
            name='image',
        ),
    ]