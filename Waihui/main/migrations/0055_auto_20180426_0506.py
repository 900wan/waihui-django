# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-26 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_auto_20180418_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_hp', models.IntegerField()),
                ('provider_hp', models.IntegerField(blank=True, null=True)),
                ('provider_active_daily', models.IntegerField(blank=True, null=True)),
                ('provider_active_course', models.IntegerField(blank=True, null=True)),
                ('provider_active_community', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ActLog',
                'verbose_name_plural': 'ActLogs',
            },
        ),
        migrations.AddField(
            model_name='log',
            name='pre_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='active_course',
            field=models.IntegerField(blank=True, default=60, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='active_daily',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AddField(
            model_name='actlog',
            name='log',
            field=models.ManyToManyField(to='main.Log'),
        ),
    ]
