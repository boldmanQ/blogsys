# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.db.models import F
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
        (3, '草稿'),
    )

    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='标题')
    describe = models.CharField(max_length=256, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须为非markdown格式')
    content_html = models.TextField(verbose_name='markdown形式正文', default='', blank=True)
    is_markdown = models.BooleanField(default=True, verbose_name='是否启用markdown解释')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey('Category', verbose_name='分类')
    tag = models.ManyToManyField('Tag', related_name='mytags', verbose_name='标签', blank=True)
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    pv = models.PositiveIntegerField(verbose_name='访问量', default=0)
    uv = models.PositiveIntegerField(verbose_name='用户量', default=0)

    def show_status(self):
        return '当前状态:%s' % self.status

    def increase_pv(self):
        return self.__class__.objects.filter(id=self.id).update(pv=F('pv') + 1)

    def increase_uv(self):
        return self.__class__.objects.filter(id=self.id).update(uv=F('uv') + 1)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
                'codehilite': {
                    'use_pygments': False,
                    'css_class': 'prettyprint linenums',
                }
            }
            self.content = self.content_html
            self.content_html = markdown.markdown(self.content_html, extensions=['codehilite'], extension_configs=config)
        else:
            self.content_html = self.content
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-created_time']


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'
