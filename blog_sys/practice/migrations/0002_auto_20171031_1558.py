# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='writter',
            field=models.ManyToManyField(to='practice.Auther', verbose_name='\u8457\u4f5c\u4eba'),
        ),
        migrations.AlterField(
            model_name='auther',
            name='age',
            field=models.IntegerField(verbose_name='\u5e74\u9f84'),
        ),
    ]
