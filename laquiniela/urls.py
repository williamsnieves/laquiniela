from django.conf.urls import url, patterns, include
from rest_framework import viewsets, routers
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'laquiniela.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'main.views.enter', name='enter'),
    url(r'^$', 'main.views.init_app', name='init_app'),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('footballpools.urls')),
    url('', include('calendars.urls')),
    url('', include('teams.urls')),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^test/$', 'main.views.test_quiniela', name='test-quiniela'),
    url(r'^dashboard/$', 'main.views.dashboard', name='quiniela'),
    url(r'^equipos/$', 'main.views.equipos', name='equipos'),
    url(r'^estadios/$', 'main.views.estadios', name='estadios'),
    url(r'^quiniela/fase-de-grupos$', 'main.views.quinielas', name='quinielas'),
    url(r'^quiniela/octavos$', 'main.views.quinielas_octavos', name='octavos'),
    url(r'^quiniela/cuartos$', 'main.views.quinielas_cuartos', name='cuartos'),
    url(r'^quiniela/semis$', 'main.views.quinielas_semis', name='semis'),
    url(r'^quiniela/final$', 'main.views.quinielas_final', name='final'),
    url(r'^fase-de-grupos/$', 'main.views.fase', name='fase'),
    url(r'^eliminatorias/$', 'main.views.eliminatorias', name='eliminatorias'),
    url(r'^login/$', 'main.views.login', name='login'),
    url(r'^log-out/$', 'main.views.log_out', name='log-out'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

