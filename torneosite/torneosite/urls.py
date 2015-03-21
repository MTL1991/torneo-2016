from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from ppal.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pdf/', some_view, name='pdf'),
)

urlpatterns += patterns('',
    url(r'^$', index, name='index'),
    url(r'^complete/$', index_all, name='index_all'),
    url(r'^us/$', us, name='us'),
    url(r'^login/$', school_login, name='login_school'),
    url(r'^accounts/login/$', school_login, name='login_school'),
    url(r'^logout/$', school_logout, name='logout_school'),
    url(r'^school/create/$', create_school, name='add_school'),    
    url(r'^school/profile/(\d+)/$', school_view, name='profile_school'),
)
urlpatterns += patterns('',
    url(r'^team/add/$', create_team, name='add_team'),
    url(r'^team/(?P<pk>\d+)/$', team_view, name='view_team'),
    url(r'^team/(?P<pk>\d+)/delete/$', TeamDelete.as_view(), name='delete_team'),
    url(r'^team/(?P<pk>\d+)/add/$', create_player, name='add_player'),
    url(r'^team/(?P<pk>\d+)/pdf$', some_view, name='pdf'),
    url(r'^player/(?P<pk>\d+)/delete$', PlayerDelete.as_view(), name='delete_player'),     
    url(r'^player/(?P<pk>\d+)', player_view, name='view_player'),  
)