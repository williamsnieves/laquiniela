from django.conf.urls import url, patterns, include
from rest_framework import viewsets, routers
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'laquiniela.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^$', 'main.views.enter', name='enter'),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('footballpools.urls')),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^test/$', 'main.views.test_quiniela', name='test-quiniela'),
    url(r'^login/$', 'main.views.enter', name='enter'),
    url(r'^log-out/$', 'main.views.log_out', name='log-out'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

