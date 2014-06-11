from django.conf.urls import patterns, url, include
from rest_framework import routers 
from rest_framework.urlpatterns import format_suffix_patterns
from calendars import views



# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = patterns('',
	url(r'^api/calendario/$', views.CalendarList.as_view()),
    url(r'^api/calendario/(?P<pk>[0-9]+)$', views.CalendarDetail.as_view()),    
    url(r'^api/calendario/(?P<city_match>.+)/$', views.CalendarList.as_view()),
    url(r'^api/oficialsmatches/$', views.CalendarioList.as_view()),
)


#urlpatterns = format_suffix_patterns(urlpatterns)
