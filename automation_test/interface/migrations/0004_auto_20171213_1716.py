# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-13 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_auto_20171213_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface_cases',
            name='testcases_updatetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='interface_cases',
            name='testcases_updator',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
