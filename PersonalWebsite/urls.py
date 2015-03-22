from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PersonalWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home),
    url(r'^/$', home),
    url(r'^portofolio$', portofolio),
    url(r'^portofolio/$', portofolio),
    url(r'^projects/([a-zA-Z0-9_]+)$', project_handler),
    url(r'^projects/([a-zA-Z0-9_]+)/$', project_handler),
    url(r'^career$', career),
    url(r'^career/$', career),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', anything),
)
