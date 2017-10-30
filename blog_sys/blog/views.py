# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.db import connection
# Create your views here.

from .models import Post, Tag, Category
from config.models import SideBar
from pprint import pprint


def post_list(request, category_id=None, tag_id=None):
    '''
    首页(列表页)
    '''
    PostData = Post.objects.all()
    # 分类页面
    if category_id:
        PostData = Post.objects.filter(category_id=category_id)
    # 标签页面
    elif tag_id:
        # queryset = Post.objects.filter(tag=tag_id)
        PostData = Tag.objects.get(id=tag_id)
        if PostData:
            PostData = PostData.mytags.all()
        else:
            PostData = []
        # queryset = Post.objects.filter(tag=tag_id)
        # queryset = queryset.filter(tag_id=tag_id)

    # 分页部分
    page = request.GET.get('page', 1)
    page_size = 4
    try:
        Page = int(page)
    except TypeError:
        Page = 1
    paginator = Paginator(PostData, page_size)

    try:
        Posts = paginator.page(page)
    except EmptyPage:
        Posts = paginator.page(paginator.num_pages)
    #pprint(dir(Posts))

    #pprint(Posts.object_list)

    # 导航栏: category
    Categorys = Category.objects.filter(status=1)
    category_is_nav = []
    category_no_nav = []
    for i in Categorys:
        if i.is_nav:
            category_is_nav.append(i)
        else:
            category_no_nav.append(i)
    

    # 模版数据
    context = {
        'POST': Posts,
        'NAVIGATION_CATEGORY': category_is_nav,
        'NO_NAVIGATION_CATEGORY': category_no_nav,
    }

    print connection.queries
    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, pk=None):
    '''
    文章详情页面
    ''' 
    print '-----------------------'
    pprint(dir(request))
    pprint(pk)
    queryset = Post.objects.get(id=pk)
    pprint(queryset.title)
    print '-----------------------'
    context = {
        'post': queryset,
    }
    return render(request, 'blog/post_detail.html', context=context)
