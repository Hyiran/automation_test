# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-13 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0002_auto_20171213_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_module',
            name='module_updatetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='project_module',
            name='module_updator',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
