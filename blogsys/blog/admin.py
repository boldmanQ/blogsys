# -*- coding: utf-8 -*-
#from django.utils.html import format_html
#from django.core.urlresolvers import reverse
from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag
from .adminform import PostAdminForm
from system.admin import BaseOwnerAdmin


class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title',
        'category',
        'get_tag',
        'show_status',
        'owner',
        'created_time',
        'pv',
        'uv',
    ]
    list_display_links = []
    # list_editable = ['title']
    search_fields = ['category__name']
    # 动作栏位置
    actions_on_top = True
    # 动作栏后的统计计数器
    actions_selection_counter = True
    # 头部时间筛选栏
    date_hierarchy = 'created_time'

    # 编辑页面 #
    # 文章保存、退出栏位置, 默认为底部
    save_on_top = True
    # save_on_bottom = False
    filter_horizontal = ('tag',)
    fieldsets = [
        ('基础信息', {'fields': [('title', 'category'), 'status', 'tag']}),
        ('文章内容', {'fields': [('describe', 'content', 'is_markdown')]}),
    ]
    #exclude = ['owner']

    def get_tag(self, obj):
        '''
        组织外键:post.tag
        '''
        return '、'.join([Mobj.name for Mobj in obj.tag.all()])
    get_tag.short_description = '标签'

    def show_status(self, obj):
        if obj.status == 1:
            return '正常'
        else:
            return '异常'
    show_status.short_description = '状态'


class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'created_time', 'status', 'owner']
    fieldsets = [
        ('定义标签', {'fields': ['name', 'status', 'is_nav']}),
    ]
    exclude = ['owner']


class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'owner']
    fields = ('name', 'status', 'owner')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
