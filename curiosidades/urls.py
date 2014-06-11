from django.conf.urls import patterns, url, include
from rest_framework import routers 
from rest_framework.urlpatterns import format_suffix_patterns
from curiosidades import views



# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = patterns('',
	url(r'^api/curiosidades/$', views.CuriosidadList.as_view()), 
)


#urlpatterns = format_suffix_patterns(urlpatterns)