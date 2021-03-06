# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-11 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shakha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gat',
            name='shakha',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shakha.Shakha'),
        ),
        migrations.AlterField(
            model_name='ghosh',
            name='rachna',
            field=models.IntegerField(default=0, verbose_name='No. of Rachnas'),
        ),
        migrations.AlterField(
            model_name='sshakha',
            name='gat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shakha.Gat'),
        ),
        migrations.AlterField(
            model_name='sshakha',
            name='swaymsevak_type',
            field=models.CharField(blank=True, choices=[('1', 'Bal'), ('2', 'Tarun'), ('3', 'Shishu'), ('4', 'Praudh')], default='1', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='swaymsevak',
            name='shakha',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shakha.Shakha'),
        ),
    ]
