from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import home, portofolio, project_handler, academic_career, skill_chart, contact, professional_career, anything, blog

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PersonalWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/?$', home),
    url(r'^portofolio/?$', portofolio),
    url(r'^projects/([a-zA-Z0-9_]+)/?$', project_handler),
    url(r'^career/academic/?$', academic_career),
    url(r'^career/professional/?$', professional_career),
    url(r'^charts/skill$', skill_chart),
    url(r'blog/?$', blog),
    url(r'^contact/?$', contact),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', anything),
)
