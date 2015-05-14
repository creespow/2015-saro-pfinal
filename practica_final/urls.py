from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practica_final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','webapp.views.begin'),
    url(r'^static/(?P<path>.*)$', "django.views.static.serve",
{'document_root': settings.STATIC_URL}),

    url(r'^login/$','webapp.views.make_login'),
    url(r'^private/$','webapp.views.private'),
    url(r'^logout/$', 'webapp.views.make_logout'),




    url(r'^admin/', include(admin.site.urls)),
)
