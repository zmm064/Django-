from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    gender_choices = [('male', '男'), ('female', '女')]

    nick_name = models.CharField('昵称', max_length=50, default='')
    birday    = models.DateField('生日', null=True, blank=True)
    gender    = models.CharField(choices=gender_choices, default='female', max_length=6)
    address   = models.CharField(max_length=100, default='')
    mobile    = models.CharField(max_length=11, blank=True)
    image     = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = '用户信息'
        #verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    send_type_choices = [('register', '注册'), ('forget', '找回密码')]

    code      = models.CharField('验证码', max_length=20)
    email     = models.EmailField('邮箱', max_length=50)
    send_type = models.CharField('验证码类型', choices=send_type_choices, max_length=10)
    send_time = models.DateTimeField('发送时间', default=datetime.now) # 这里对now不加括号，这样就不会在被编译时调用，而是在实例化时被调用

    class Meta:
        verbose_name = '邮箱验证码'
        #verbose_name_plural = verbose_name

    def __str__(self):
        return '{} ({})'.format(self.code, self.email)

class Banner(models.Model):
    title    = models.CharField('标题', max_length=100)
    image    = models.ImageField('轮播图文件地址', max_length=100, upload_to='banner/%Y/%m')
    url      = models.URLField('访问地址', max_length=200)
    index    = models.IntegerField('顺序', default=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        #verbose_name_plural = verbose_name

