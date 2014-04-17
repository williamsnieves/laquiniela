from footballpools.models import FootballPool
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