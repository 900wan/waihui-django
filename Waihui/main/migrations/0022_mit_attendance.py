# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20160710_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='mit_attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'mit_attendance',
                'verbose_name_plural': 'mit_attendances',
            },
        ),
    ]
