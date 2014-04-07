from django.conf.urls import patterns, url, include
from rest_framework import routers
from footballpools.views import FootballPoolViewSet 


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'footballpools', FootballPoolViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)