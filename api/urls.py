from django.conf.urls import patterns, url


urlpatterns = patterns(
	'api.views',
	url(r'^positions/$', 'positions'),
	#url(r'^position/(?P<pk>[A-Z]+)$', 'group_position'),
	url(r'^position/(?P<group>[-A-Za-z0-9_]+)/$', 'group_position'),

)