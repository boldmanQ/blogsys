#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zq time:2018/3/15
from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    '''
    1.用来处理文章、分类、标签、侧边栏、友链这些model的owner子段自动补充
    2.用来针对queryset过滤当前用户的数据
    '''
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset.all()
        return queryset.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
