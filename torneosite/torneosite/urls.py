from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from ppal.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pdf/', some_view, name='pdf'),
    url(r'^plano/',plano_view, name='plano_view'),
)

urlpatterns += patterns('',
    url(r'^$', select_years, name='choose_years'),
    url(r'^matchs/', index, name='index'),
    url(r'^teams/', teams, name='teams'),
    url(r'^sub9/group/(?P<pk>\d+)/$', group_view1, name='group_view_sub9'),
    url(r'^sub9/eliminatoria/', eliminatoria_view1, name='eliminatoria_view_sub9'),
    url(r'^sub19/groups$', group_view1_all, name='group_view1_all'),
    url(r'^sub12/groups$', group_view2_all, name='group_view2_all'),
    url(r'^sub12/group/(?P<pk>\d+)/$', group_view2, name='group_view_sub12'),
    url(r'^sub12/eliminatoria/', eliminatoria_view2, name='eliminatoria_view_sub12'),
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
    url(r'^team/(?P<pk>\d+)/edit/$', TeamUpdate.as_view(), name='update_team'),
    url(r'^team/(?P<pk>\d+)/pdf$', some_view, name='pdf'),
    url(r'^player/(?P<pk>\d+)/delete$', PlayerDelete.as_view(), name='delete_player'),     
    url(r'^player/(?P<pk>\d+)', player_view, name='view_player'),  
    url(r'^match/add/$', create_match, name='add_match'),
    url(r'^match/all$', view_all_match, name='view_all_match'),
    url(r'^match/pabellon$', view_pabellon_match, name='view_pabellon_match'),
    url(r'^match/baloncesto$', view_baloncesto_match, name='view_baloncesto_match'),
    url(r'^match/sala$', view_sala_match, name='view_sala_match'),
    url(r'^match/(?P<pk>\d+)$', match_view, name='match_view'),
    url(r'^match/(?P<pk>\d+)/edit$', MatchUpdate.as_view(), name='update_match'),
    url(r'^match/(?P<pk>\d+)/result$', ResultUpdate.as_view(), name='update_result'),
    url(r'^match/(?P<pk>\d+)/octavos$', OctavosUpdate.as_view(), name='update_octavos'),
    url(r'^match/(?P<pk>\d+)/cuartos$', CuartosUpdate.as_view(), name='update_cuartos'),
    url(r'^match/(?P<pk>\d+)/semis$', FinalUpdate.as_view(), name='update_semis'),
)
urlpatterns += patterns('',
    url(r'^group/sub9/(?P<pk>\d+)/$', group_view1, name='group_view_sub9'),
    url(r'^group/sub12/(?P<pk>\d+)/$', group_view2, name='group_view_sub12'),
    url(r'^eliminatoria/sub9', eliminatoria_view1, name='eliminatoria_view_sub9'),
    url(r'^eliminatoria/sub12', eliminatoria_view2, name='eliminatoria_view_sub12'),
    #url(r'^group/add$', create_group, name='create_group'),
)