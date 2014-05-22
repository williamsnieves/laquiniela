from django.conf.urls import patterns, url


urlpatterns = patterns(
	'api.views',
	url(r'^matches/$', 'matches_qnl'),
	url(r'^positions/qnl/$', 'positions_qnl'),
	url(r'^positions/$', 'positions'),
	url(r'^quiniela/$', 'quiniela'),
	url(r'^quiniela/new$', 'nueva_quiniela'),
	url(r'^quiniela/count$', 'get_totalqnl'),
	url(r'^quiniela/progress$', 'get_progressqnl'),
	url(r'^quiniela/fase$', 'get_completefaseqnl'),
	url(r'^quiniela/eliminatoria$', 'get_eliminatoria'),
	url(r'^quiniela/valid$', 'get_validqnl'),
	#url(r'^position/(?P<pk>[A-Z]+)$', 'group_position'),
	url(r'^position/(?P<group>[-A-Za-z0-9_]+)/$', 'group_position'),
	url(r'^positions/qnlgroup/$', 'group_position_qnl'),

)