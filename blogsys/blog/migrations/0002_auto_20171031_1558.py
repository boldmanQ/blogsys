# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_nav',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e3a\u5bfc\u822a'),
        ),
        migrations.AlterField(
            model_name='post',
            name='describe',
            field=models.CharField(blank=True, max_length=128, verbose_name='\u6458\u8981'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='mytags', to='blog.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]