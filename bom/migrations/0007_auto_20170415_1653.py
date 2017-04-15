# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0006_auto_20170415_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SellerPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_order_quantity', models.IntegerField(blank=True, null=True)),
                ('minimum_pack_quantity', models.IntegerField(blank=True, null=True)),
                ('unit_cost', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('lead_time_days', models.IntegerField(blank=True, null=True)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Part')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Seller')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sellerpart',
            unique_together=set([('seller', 'part', 'minimum_order_quantity', 'unit_cost')]),
        ),
    ]
