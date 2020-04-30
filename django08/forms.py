"""
@author: wanghongliang
@file: forms.py
@time: 2020/4/30 9:37 
"""
from django import forms
from django08 import models
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ]
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='王大人')
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)
    user_school = forms.BooleanField(label='是否在学', required=False)
    user_email = forms.EmailField(label='电子邮件')
    user_message = forms.CharField(label='您的意见', widget=forms.Textarea)


class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Post
        fields = ['mood', 'nickname', 'message', 'del_pass']

    # 不写这个会显示原来的列名
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '现在心情'
        self.fields['nickname'].label = '你的昵称'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '设置密码'
        self.fields['captcha'].label = '确定你不是机器人'
