#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zq time:2018/3/15
from django.contrib import admin

from blog.models import Category


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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category' and not request.user.is_superuser:
            kwargs["queryset"] = Category.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
