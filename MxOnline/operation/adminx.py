import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse

class UserAskAdmin:
    list_display  = ['name', 'mobile', 'course_name', 'add_time']
    list_filter   = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']


class CourseCommentsAdmin:
    list_display  = ['user', 'course', 'comments', 'add_time']
    list_filter   = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']


class UserFavoriteAdmin:
    list_display  = ['user', 'fav_id', 'fav_type', 'add_time']
    list_filter   = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']


class UserMessageAdmin:
    list_display  = ['user', 'message', 'has_read', 'add_time']
    list_filter   = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']


class UserCourseAdmin:
    list_display  = ['user', 'course', 'add_time']
    list_filter   = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)

