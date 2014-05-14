from django.conf.urls import patterns, url


urlpatterns = patterns(
	'api.views',
	url(r'^matches/$', 'matches_qnl'),
	url(r'^positions/qnl/$', 'positions_qnl'),
	url(r'^positions/$', 'positions'),
	url(r'^quiniela/$', 'quiniela'),
	url(r'^quiniela/new$', 'nueva_quiniela'),
	#url(r'^position/(?P<pk>[A-Z]+)$', 'group_position'),
	url(r'^position/(?P<group>[-A-Za-z0-9_]+)/$', 'group_position'),
	url(r'^position/qnl/(?P<group>[-A-Za-z0-9_]+)/$', 'group_position_qnl'),

)