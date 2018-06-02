# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from blogsys.adminx import BaseOwnerAdmin
from .models import Comment


class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'content', 'nickname', 'website', 'email', 'created_time')
    search_fields = ['nickname', ]


xadmin.site.register(Comment, CommentAdmin)
