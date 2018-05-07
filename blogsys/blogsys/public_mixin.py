#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zq time:2018/4/25

from comment.forms import CommentForm
from comment.models import Comment


class CommentShowMixin(object):

    def get_comments(self):
        target = self.request.path
        return Comment.objects.filter(target=target)

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(initial={'target': self.request.path}),
            'comment_list': self.get_comments()
        })
        return super(CommentShowMixin, self).get_context_data(**kwargs)
