from django.conf.urls import patterns, url, include
from rest_framework import routers 
from rest_framework.urlpatterns import format_suffix_patterns
from teams import views



# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = patterns('',
	url(r'^equipos/$', views.TeamList.as_view()),
    url(r'^equipos/(?P<pk>[0-9]+)$', views.TeamDetail.as_view()),    
)


#urlpatterns = format_suffix_patterns(urlpatterns)