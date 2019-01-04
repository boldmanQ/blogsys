# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from blog.views import CommonMixin

from .models import Link
from comment.forms import CommentForm


class LinkView(CommonMixin, ListView):
    queryset = Link.objects.filter(status=1)
    template_name = 'config/links.html'
    context_object_name = 'links'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm
        })
        return super().get_context_data(**kwargs)
