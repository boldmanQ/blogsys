# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from blogsys.adminx import  BaseOwnerAdmin
from .models import Link, SideBar


class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'weight', 'owner', 'edit_operator')

    def edit_operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:config_link_change', args=(obj.id,))
        )
    edit_operator.short_description = '编辑'
xadmin.site.register(Link, LinkAdmin)


class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'content', 'content', 'owner', 'created_time')
xadmin.site.register(SideBar, SideBarAdmin)

