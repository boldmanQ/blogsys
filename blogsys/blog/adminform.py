#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zq time:2018/3/1
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label='是否删除', required=False)
    describe = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    content = forms.CharField(widget=CKEditorUploadingWidget())

    def clean_status(self):
        if self.cleaned_data['status']:
            return 2
        else:
            return 1
