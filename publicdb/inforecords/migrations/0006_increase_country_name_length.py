# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-29 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inforecords', '0005_fix_ip_fields_bug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]
