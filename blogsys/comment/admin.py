# -*- coding: utf-8 -*-

from django.contrib import admin

from system.admin import BaseOwnerAdmin
from .models import Comment


class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'content', 'nickname', 'website', 'email', 'created_time')
    search_fields = ['nickname', ]


admin.site.register(Comment, CommentAdmin)
