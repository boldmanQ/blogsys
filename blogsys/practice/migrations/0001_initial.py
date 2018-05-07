# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='\u4f5c\u8005')),
                ('age', models.IntegerField(max_length=3, verbose_name='\u5e74\u9f84')),
            ],
            options={
                'verbose_name': '\u8457\u4f5c\u4eba\u4fe1\u606f',
                'verbose_name_plural': '\u8457\u4f5c\u4eba\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=50, verbose_name='\u51fa\u7248\u5546')),
                ('title', models.CharField(max_length=30, verbose_name='\u4e66\u540d')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4e66\u7c4d',
                'verbose_name_plural': '\u4e66\u7c4d',
            },
        ),
    ]