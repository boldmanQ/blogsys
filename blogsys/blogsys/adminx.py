#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zq time:2018/3/15

from __future__ import unicode_literals

import xadmin
from xadmin.views import CommAdminView


class BaseOwnerAdmin(object):
    '''
    1.用来处理文章、分类、标签、侧边栏、友链这些model的owner子段自动补充
    2.用来针对queryset过滤当前用户的数据
    '''
    def get_list_queryset(self):
        request = self.request
        queryset = super(BaseOwnerAdmin, self).get_list_queryset()
        if request.user.is_superuser:
            return queryset.all()
        return queryset.filter(owner=request.user)

    def save_models(self):
        # import pdb;pdb.set_trace()
        if not self.org_obj:
            self.new_obj.owner = self.request.user
        return super(BaseOwnerAdmin, self).save_models()


class XAdminGlobalSetting(object):
    site_title = '車乞的博客后台'
    site_footer = 'power by zhangqianlinux@qq.com'


xadmin.site.register(CommAdminView, XAdminGlobalSetting)
