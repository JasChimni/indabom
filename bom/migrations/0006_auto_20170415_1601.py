# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0005_auto_20170309_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='minimum_order_quantity',
        ),
        migrations.RemoveField(
            model_name='part',
            name='minimum_pack_quantity',
        ),
        migrations.RemoveField(
            model_name='part',
            name='unit_cost',
        ),
    ]
