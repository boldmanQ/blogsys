# -*- coding: utf-8 -*-
import uuid

from django.core.cache import cache
from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category
from extra.models import SideBar, Link
#from comment.models import Comment
from system.public_mixin import CommentShowMixin


class CommonMixin(object):
    def get_context_data(self, **kwargs):
        categories = Category.objects.filter(status=1)

        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)

        side_bars = SideBar.objects.filter(status=1)

        recently_posts = Post.objects.filter(status=1)[:7]
        # recently_comments = Comment.objects.all()[:5]
        hot_posts = Post.objects.filter(status=1).order_by('-pv')[:7]
        links = Link.objects.all()

        extra_context = {
            'NAVIGATION_CATEGORY': nav_cates,
            'NO_NAVIGATION_CATEGORY': cates,
            'SIDEBAR': side_bars,
            'HOT_POST': hot_posts,
            'NEW_POST': recently_posts,
            'LINKS': links,
            # 'NEW_COMMENT': recently_comments,
        }

        extra_context.update(kwargs)
        return super().get_context_data(**extra_context)


class BasePostView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'POST'
    paginate_by = 5

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if 'sessionid' not in self.request.COOKIES:
            response.set_cookie('sessionid', uuid.uuid4().hex)
        return response


class IndexView(BasePostView):
    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = super().get_queryset()
        if not query:
            return qs.filter(status=1)
        res = qs.filter(title__icontains=query).filter(status=1)
        return res

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super().get_context_data(query=query)


class CategoryView(BasePostView):
    def get_queryset(self):
        qs = super().get_queryset()
        category = self.kwargs['category_name']
        qs = qs.filter(category__name=category).filter(status=1)
        return qs


class TagView(BasePostView):
    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []
        posts = tag.mytags.all().filter(status=1)
        return posts


class PostView(CommonMixin, CommentShowMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'POST'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        #增加pv, 半小时内重复请求无效
        #增加uv，24小时内重复请求无效

        post_path = self.request.path
        if 'sessionid' not in self.request.COOKIES:
            return
        sessionid = self.request.COOKIES['sessionid']

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
        author = self.kwargs.get('username')
        qs = super().get_queryset()
        #import ipdb;ipdb.set_trace()
        if author:
            qs = qs.filter(owner__username=author).filter(status=1)
        return qs.filter(status=1)
