# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 12:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_mit_attendance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mit_attendance',
        ),
    ]
