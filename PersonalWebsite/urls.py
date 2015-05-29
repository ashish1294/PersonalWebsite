from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import home, portofolio, project_handler, academic_career,\
    skill_chart, contact, professional_career, anything, blog, site_map, \
    search, about_me, achievement, add_testimonial

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PersonalWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/?$', home),
    url(r'^portofolio/?$', portofolio),
    url(r'^portfolio/?$', portofolio),
    url(r'^skills/?$', portofolio),
    url(r'^abilities/?$', portofolio),
    url(r'^projects/([a-zA-Z0-9_]+)/?$', project_handler),
    url(r'^project/([a-zA-Z0-9_]+)/?$', project_handler),
    url(r'^career/?$', academic_career),
    url(r'^career/academic/?$', academic_career),
    url(r'^career/professional/?$', professional_career),
    url(r'^charts/skill$', skill_chart),
    url(r'blog/?$', blog),
    url(r'^addtestimonial/?$', add_testimonial),
    url(r'^add_testimonial/?$', add_testimonial),
    url(r'^testimonial_add/?$', add_testimonial),
    url(r'^contact/?$', contact),
    url(r'^aboutme/?$', about_me),
    url(r'^about_me/?$', about_me),
    url(r'^achievements/?$', achievement),
    url(r'^sitemap/?$', site_map),
    url(r'^search/?', search),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)$', anything),
)