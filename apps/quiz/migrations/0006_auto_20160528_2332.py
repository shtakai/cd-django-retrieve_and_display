# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 23:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20160528_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='musician',
        ),
        migrations.RemoveField(
            model_name='car',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='customerdetail',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='topping',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='CustomerDetail',
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
