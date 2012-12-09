from django.conf.urls import patterns, include, url
from games.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'games.views.Home'),
<<<<<<< HEAD
    url(r'^login$', 'games.views.Login'),
    url(r'^shanghigames/(?P<gameid>\d+)$', 'games.views.addScore'),
=======
    url(r'^shanghigame/(?P<gameid>\d+)$', 'games.views.addScore'),
>>>>>>> 5b411ffef962b06343189b6329dae0010a9171c7
    # url(r'^darts/', include('darts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
