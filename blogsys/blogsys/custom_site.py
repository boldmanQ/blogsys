#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zq time:2018/3/15

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = '张乾的博客'
    site_title = '管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
'''
custom_site.register(PostAdmin)
'''
