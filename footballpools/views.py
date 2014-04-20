from footballpools.models import FootballPool
from footballpoolsusers.models import FootballPoolUser
from calendars.models import Calendar
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from footballpools.serializers import FootballPoolSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
# ViewSets define the view behavior.

"""class FootballPoolViewSet(viewsets.ModelViewSet):
    queryset = FootballPool.objects.all()
    serializer_class = FootballPoolSerializer"""


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FootballPoolList(generics.ListCreateAPIView):
    queryset = FootballPool.objects.all()
    serializer_class = FootballPoolSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
    	obj.user_qnl = self.request.user


class FootballPoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FootballPool.objects.all()
    serializer_class = FootballPoolSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
    	obj.user_qnl = self.request.user


def nueva_quiniela(request):
    print("creo nueva quiniela")
    c1 = Calendar.objects.all()
    for item in c1:
        quiniela = FootballPool(cod_qnl='aa5',user_qnl=18,group_qnl=item.group_match,date_qnl=item.date_match,name_qnl=item.name_match,team_a_qnl=item.team_a_match,goals_a_qnl=0,team_b_qnl=item.team_b_match,goals_b_qnl=0,result_qnl='0-0')
        quiniela.save()
    return HttpResponse("creando quiniela")