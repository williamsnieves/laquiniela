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

    def get_queryset(self):
        queryset = FootballPool.objects.all()
        userqnl = self.request.QUERY_PARAMS.get('username', None)
        groupqnl = self.request.QUERY_PARAMS.get('group', None)

        if userqnl is not None:
            queryset = queryset.filter(user_qnl=userqnl)
        elif groupqnl is not None:
            queryset = queryset.filter(group_qnl=groupqnl)

        return queryset


class FootballPoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FootballPool.objects.all()
    serializer_class = FootballPoolSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
    	obj.user_qnl = self.request.user

    def get_queryset(self):
        queryset = FootballPool.objects.all()
        userqnl = self.request.QUERY_PARAMS.get('username', None)
        groupqnl = self.request.QUERY_PARAMS.get('group', None)

        if userqnl is not None:
            queryset = queryset.filter(user_qnl=userqnl)
        elif groupqnl is not None:
            queryset = queryset.filter(group_qnl=groupqnl)

        return queryset


def nueva_quiniela(request):
    print("creo nueva quiniela")
    quiniela_user = FootballPoolUser(cod_qnl='test',username=request.user.username)
    quiniela_user.save()
    quiniela_last_id = FootballPoolUser.objects.latest('id')
    quiniela_current = FootballPoolUser.objects.get(pk=quiniela_last_id.id)
    correlativo_quiniela = str(quiniela_current.id)+quiniela_current.username
    #print(correlativo_quiniela)
    quiniela_current.cod_qnl = correlativo_quiniela
    quiniela_current.save()

    c1 = Calendar.objects.all()
    for item in c1:
        quiniela = FootballPool(cod_qnl=quiniela_current.cod_qnl,user_qnl=request.user,group_qnl=item.group_match,date_qnl=item.date_match,name_qnl=item.name_match,team_a_qnl=item.team_a_match,goals_a_qnl=0,team_b_qnl=item.team_b_match,goals_b_qnl=0,result_qnl='0-0')
        quiniela.save()
    return HttpResponse("creando quiniela")