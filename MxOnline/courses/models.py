from datetime import datetime

from django.db import models

# Create your models here.
class Course(models.Model):
    degree_choices = [('cj', '初级'), ('zj', '中级'), ('gj', '高级')]

    name         = models.CharField('课程名', max_length=50)
    desc         = models.CharField('课程描述', max_length=300)
    detail       = models.TextField('课程详情')
    degree       = models.CharField('课程难度', max_length=2, choices=degree_choices)
    learn_times  = models.IntegerField('学习时长(分钟数)', default=0)
    students     = models.IntegerField('学习人数', default=0)
    fav_nums     = models.IntegerField('收藏人数)', default=0)
    image        = models.ImageField('封面图', max_length=100, upload_to="courses/%Y%m")
    click_number = models.IntegerField('点击数', default=0)
    add_time     = models.DateTimeField('添加时间', default=datetime.now)


    class Meta:
        verbose_name = '课程'
        #verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    

class CourseResource(models.Model):
    name     = models.CharField('资源名', max_length=100)
    download = models.FileField('资源地址',max_length=100, upload_to='course/resource/%Y/%m')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    course   = models.ForeignKey(Course, verbose_name='课程')

    class Meta:
        verbose_name = '课程资源'
        #verbose_name_plural = verbose_name



class Lesson(models.Model):
    name     = models.CharField('章节名', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    course   = models.ForeignKey(Course, verbose_name='课程名')

    class Meta:
        verbose_name = '章节'
        #verbose_name_plural = verbose_name


class Video(models.Model):
    name     = models.CharField('视频名', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    lesson   = models.ForeignKey(Lesson, verbose_name='章节名')

    class Meta:
        verbose_name = '视频'
        #verbose_name_plural = verbose_name
