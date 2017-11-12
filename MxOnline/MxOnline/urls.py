from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin


from users.views import LoginView

urlpatterns = [
    # Examples:
    # url(r'^$', MxOnline.views.home, name='home'),
    # url(r'^MxOnline/', include('MxOnline.MxOnline.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
]
