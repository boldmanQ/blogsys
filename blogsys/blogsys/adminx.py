#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zq time:2018/3/15

from __future__ import unicode_literals

import xadmin
from django.contrib import admin


class BaseOwnerAdmin(object):
    '''
    1.用来处理文章、分类、标签、侧边栏、友链这些model的owner子段自动补充
    2.用来针对queryset过滤当前用户的数据
    '''
    exclude = ('owner', )

    def get_list_queryset(self):
        request = self.request
        queryset = super(BaseOwnerAdmin, self).get_list_queryset()
        if request.user.is_superuser:
            return queryset.all()
        return queryset.filter(owner=request.user)

    def save_models(self):
        #print(self, request, obj, form, change)
        obj.owner = self.request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
11