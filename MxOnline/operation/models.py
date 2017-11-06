from django.db import models
from datetime import datetime

from users.models import UserProfile
from courses.models import Course
# Create your models here.
class UserAsk(models.Model):
    name        = models.CharField('姓名', max_length=20)
    mobile      = models.CharField('手机', max_length=11)
    course_name = models.CharField('课程名', max_length=50)
    add_time    = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户咨询'
        #verbose_name_plural = verbose_name

class CourseComments(models.Model):
    comments = models.CharField('评论', max_length=200)
    add_time = models.DateField('添加时间', default=datetime.now)

    course   = models.ForeignKey(Course, verbose_name='课程')
    user     = models.ForeignKey(UserProfile, verbose_name='用户')

    class Meta:
        verbose_name = '添加时间'
        #verbose_name_plural = verbose_name

class UserFavorite(models.Model):
    fav_type_choice = [(1, '课程'), (1, '课程机构'), (3, '讲师')]

    fav_id   = models.IntegerField('数据id', default=0)
    fav_type = models.IntegerField('收藏类型', choices=fav_type_choice)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    user     = models.ForeignKey(UserProfile, verbose_name='用户')

    class Meta:
        verbose_name = '用户收藏'
        #verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user     = models.IntegerField('接收用户', default=0)
    message  = models.CharField('消息内容', max_length=500)
    has_read = models.BooleanField('是否已读', default=False)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户消息'
        #verbose_name_plural = verbose_name

class UserCourse(models.Model):
    user     = models.ForeignKey(UserProfile, verbose_name='用户')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    course   = models.ForeignKey(Course, verbose_name='课程')

    class Meta:
        verbose_name = '用户课程'
        #verbose_name_plural = verbose_name