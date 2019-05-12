# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from system.admin import BaseOwnerAdmin
from .models import Link, SideBar


class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'weight', 'owner', 'edit_operator')


class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'content', 'content', 'owner', 'created_time')


admin.site.register(Link, LinkAdmin)
admin.site.register(SideBar, SideBarAdmin)
