# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-17 05:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20180316_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue_book',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book'),
        ),
    ]
