#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zq time:2018/4/21

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    target = forms.CharField(
        label='评论目标',
        max_length=50,
        widget=forms.HiddenInput
    )
    nickname = forms.CharField(
        label='昵称',
        max_length=20,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.CharField(
        label='邮箱',
        max_length=20,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    website = forms.CharField(
        label='网址',
        max_length=20,
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control'}
        )
    )
    content = forms.CharField(
        label='内容',
        max_length=500,
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-control'}
        )
    )

    # def __init__(self, target=None, *args, **kwargs):
    #     if target:
    #         self.target = target
    #     super(CommentForm, self).__init__(*args, **kwargs)

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('评论的长度至少要10个文字')
        return content

    class Meta:
        model = Comment
        fields= ['target', 'nickname', 'website', 'email', 'content']