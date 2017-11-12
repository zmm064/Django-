import xadmin

from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin:
    list_display  = ['name', 'desc', 'add_time']
    list_filters  = ['name', 'desc', 'add_time']
    search_fileds = ['name', 'desc']


class CourseOrgAdmin:
    list_display  = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'add_time']
    list_filters  = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'add_time']
    search_fileds = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address']


class TeacherAdmin:
    list_display  = ['name', 'work_years', 'work_company']
    list_filters  = ['name', 'work_years', 'work_company']
    search_fileds = ['name', 'work_years', 'work_company']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
