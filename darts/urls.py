from django.conf.urls import patterns, include, url
from games.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'games.views.Home'),
    url(r'^shanghigames/(?P<gameid>\d+)$', 'games.views.addScore'),
    url(r'^login$', 'games.views.Login'),
    url(r'^logout$', 'games.views.Logout'),
    # url(r'^darts/', include('darts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
