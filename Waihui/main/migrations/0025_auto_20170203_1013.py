# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20170119_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, b'\xe4\xb8\x8d\xe5\x8f\xaf\xe6\x94\xaf\xe4\xbb\x98'), (1, b'\xe6\x9c\xaa\xe6\x94\xaf\xe4\xbb\x98'), (2, b'\xe5\xb7\xb2\xe6\x94\xaf\xe4\xbb\x98'), (3, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (4, b'\xe7\x94\xb3\xe8\xaf\xb7\xe9\x80\x80\xe6\xac\xbe'), (5, b'\xe5\xb7\xb2\xe9\x80\x80\xe6\xac\xbe'), (6, b'\xe5\xb7\xb2\xe9\x9a\x90\xe8\x97\x8f')], default=1),
        ),
    ]
