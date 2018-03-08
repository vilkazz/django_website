# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_press'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='type',
            field=models.IntegerField(choices=[(1, 'collection'), (2, 'campaign')], default=1),
        ),
        migrations.AddField(
            model_name='press',
            name='title',
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='press',
            name='contents',
            field=models.TextField(max_length=10000),
        ),
    ]
