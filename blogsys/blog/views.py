# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from silk.profiling.profiler import silk_profile

from django.core.cache import cache
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Post, Tag, Category
from config.models import SideBar, Link
from comment.models import Comment
from blogsys.public_mixin import CommentShowMixin
from pprint import pprint


class CommonMixin(object):
    @silk_profile(name='get_context_data')
    def get_context_data(self, **kwargs):
        # context = super(CommonMixin, self).get_context_data()
        categories = Category.objects.filter(status=1)

        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)

        side_bars = SideBar.objects.filter(status=1)

        recently_posts = Post.objects.filter(status=1)[:10]
        recently_comments = Comment.objects.all()[:5]
        hot_posts = Post.objects.order_by('-pv')[:5]

        extra_context = {
            'NAVIGATION_CATEGORY': nav_cates,
            'NO_NAVIGATION_CATEGORY': cates,
            'SIDEBAR': side_bars,
            'HOT_POST': hot_posts,
            'NEW_POST': recently_posts,
            'NEW_COMMENT': recently_comments,
        }

        extra_context.update(kwargs)
        return super(CommonMixin, self).get_context_data(**extra_context)


class BasePostView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'POST'
    paginate_by = 10


class IndexView(BasePostView):
    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = super(IndexView, self).get_queryset()
        if not query:
            return qs
        res = qs.filter(title__icontains=query)
        return res

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)


class CategoryView(BasePostView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs['category_id']
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostView):
    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []
        posts = tag.mytags.all()
        return posts


class PostView(CommonMixin, CommentShowMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'POST'

    def get(self, request, *args, **kwargs):
        response = super(PostView, self).get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        #增加pv, 半小时内重复请求无效
        #增加uv，24小时内重复请求无效

        post_path = self.request.path
        sessionid = getattr(self.request.COOKIES, 'sessionid', None)
        if not sessionid:
            return

        pv_key = 'pv_key:%s,%s' % (post_path, sessionid)
        uv_key = 'uv_key:%s,%s' % (post_path, sessionid)
        if not cache.get(pv_key):
            self.object.increase_pv()
            cache.set(pv_key, 1, 60 * 30)
        if not cache.get(uv_key):
            self.object.increase_uv()
            cache.set(uv_key, 1, 60 * 60 * 24)


class AuthorView(BasePostView):
    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        qs = super(AuthorView, self).get_queryset()
        if author_id:
            qs = qs.filter(owner_id=author_id)
        return qs
