import xadmin
from .models import Course, Lesson, Video, CourseResource

class CourseAdmin:
    list_display  = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums']
    list_filter   = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums']


class LessionAdmin:
    list_display  = ['course', 'name', 'add_time']
    list_filter   = ['course__name', 'name', 'add_time'] # 双下划线指定过滤外键字段
    search_fields = ['course__name', 'name']


class VideoAdmin:
    list_display  = ['lesson', 'name', 'add_time']
    list_filter   = ['lesson__name', 'name', 'add_time'] # 双下划线指定过滤外键字段
    search_fields = ['lesson__name', 'name']


class CourseResourceAdmin:
    list_display  = ['course', 'name', 'download', 'add_time']
    list_filter   = ['course__name', 'name', 'download', 'add_time'] # 双下划线指定过滤外键字段
    search_fields = ['course__name', 'name', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessionAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
