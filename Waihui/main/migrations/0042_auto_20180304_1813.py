# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-04 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20180304_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackquestionnaireb2p',
            name='continuing',
            field=models.IntegerField(choices=[(1, '\u5341\u5206\u613f\u610f'), (2, '\u503c\u5f97\u8003\u8651'), (3, '\u4e0d\u4f1a\u4e86\uff0c\u518d\u4e5f\u4e0d\u4f1a\u4e86')], null=True, verbose_name='\u4f60\u8fd8\u4f1a\u9009\u8fd9\u4e2a\u8001\u5e08\u7684\u8bfe\u7a0b\u5417'),
        ),
        migrations.AlterField(
            model_name='feedbackquestionnaireb2p',
            name='plan',
            field=models.IntegerField(choices=[(1, '\u6761\u7406\u6e05\u695a'), (2, '\u53ea\u662f\u8fd8\u53ef\u4ee5'), (3, '\u5b8c\u5168\u770b\u4e0d\u61c2\u4ed6\u8981\u8bb2\u4ec0\u4e48')], null=True, verbose_name='\u6559\u6848\u662f\u5426\u6e05\u695a\u660e\u767d'),
        ),
        migrations.AlterField(
            model_name='feedbackquestionnaireb2p',
            name='satisfaction',
            field=models.IntegerField(choices=[(1, '0\u661f'), (2, '1\u661f'), (3, '2\u661f'), (4, '3\u661f'), (5, '4\u661f'), (6, '5\u661f')], null=True, verbose_name='\u672c\u6b21\u8bfe\u7a0b\u4f60\u5bf9\u8001\u5e08\u662f\u5426\u6ee1\u610f'),
        ),
        migrations.AlterField(
            model_name='feedbackquestionnaireb2p',
            name='teaching',
            field=models.IntegerField(choices=[(1, '\u975e\u5e38\u6e05\u695a'), (2, '\u4e00\u822c\uff0c\u52c9\u5f3a\u542c\u61c2'), (3, '\u4e0d\u6e05\u695a')], null=True, verbose_name='\u8001\u5e08\u8bb2\u8bfe\u662f\u5426\u6e05\u695a\u660e\u767d'),
        ),
    ]
