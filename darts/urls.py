from django.conf.urls import patterns, include, url
from games.views import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'games.views.Test'),
    url(r'^shanghigames/(?P<gameid>\d+)$', 'games.views.addScore'),
    url(r'^shanghigames/undo/(?P<gameid>\d+)$', 'games.views.Undo'),
    url(r'^login$', 'games.views.Login'),
    url(r'^logout$', 'games.views.Logout'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root':settings.STATIC_ROOT}),
    url(r'^creategame/$', 'games.views.SetUpShanghi'),
    url(r'^stats/$', 'games.views.Stats'),
    url(r'^creategame/makenewgame$', 'games.views.CreateShanghi'),
    url(r'^previousgames/$', 'games.views.History'),
    url(r'^player/$', 'games.views.Player'),
)
