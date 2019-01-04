# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.views.generic import TemplateView

from .forms import CommentForm
from .models import Comment
from system.public_mixin import CommentShowMixin
# Create your views here.


class CommentView(TemplateView, CommentShowMixin):
    model = Comment
    template_name = 'comment/result.html'
    http_method_names = ['POST']

    def get(self, request, *args, **kwargs):
        return super(CommentView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = comment_form.data['target']
        if comment_form.is_valid():
            print (comment_form.data)
            print (comment_form.fields)
            comment_form.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False
        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,
        }
        return self.render_to_response(context)
