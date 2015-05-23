from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practica_final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','webapp.views.begin'),
    url(r'^static/(?P<path>.*)$', "django.views.static.serve",
{'document_root': settings.STATIC_URL}),

    url(r'^save/(.*)$','webapp.views.save'),
    url(r'^makeparse/$','webapp.views.parser'),
    url(r'^todas','webapp.views.all'),
    url(r'^ayuda','webapp.views.help'),
    url(r'^private','webapp.views.private'),
    url(r'^login','webapp.views.make_login'),    
    url(r'^logout', 'webapp.views.make_logout'),
    url(r'^(.+)/rss', 'webapp.views.get_rss'),
    url(r'^(.+)', 'webapp.views.userpage')
)
