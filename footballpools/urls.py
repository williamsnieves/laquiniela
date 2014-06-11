from django.conf.urls import patterns, url, include
from rest_framework import routers 
from rest_framework.urlpatterns import format_suffix_patterns
from footballpools import views



# Routers provide an easy way of automatically determining the URL conf.
"""router = routers.DefaultRouter()
router.register(r'footballpools', FootballPoolViewSet)"""

"""urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)"""

urlpatterns = patterns('',
    url(r'^testy/list$', views.FootballPoolList.as_view()),
    url(r'^testy/(?P<pk>[0-9]+)$', views.FootballPoolDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
	url(r'^api/quinielas/$', views.FootballPoolList.as_view()),
)


#urlpatterns = format_suffix_patterns(urlpatterns)
