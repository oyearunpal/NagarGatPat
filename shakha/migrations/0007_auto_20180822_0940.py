# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-08-22 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakha', '0006_auto_20180320_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='sshakha',
            name='ganvesh_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='spersonal',
            name='basti',
            field=models.CharField(choices=[('1', 'Satynagar'), ('2', 'Krishna'), ('3', 'Ramjanki'), ('4', 'Umamaheswar'), ('5', 'Lalbahadur Shahstri'), ('6', 'Shree Durga'), ('7', 'Netaji Nagar'), ('8', 'Kajupada'), ('9', 'SunderBag Paschim'), ('10', 'SunderBag Purv')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='sshakha',
            name='jimmedari',
            field=models.CharField(choices=[('0', 'Tat'), ('1', 'Pat'), ('2', 'Gatnayak'), ('3', 'Upgatnayak'), ('4', 'Vyastha Pramukh'), ('5', 'Geet Pramukh'), ('6', 'Khel Pramukh'), ('7', 'Gan Shikshak'), ('8', 'Prathna Pramukh'), ('9', 'Mukhy Shikshak'), ('10', 'Shakha Karyvah'), ('11', 'Palak'), ('12', 'Nagar'), ('13', 'Other')], default='1', max_length=2),
        ),
    ]
