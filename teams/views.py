from teams.models import Team
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from teams.serializers import TeamSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

# Create your views here.

class EquipoList(generics.ListAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

	def get_queryset(self):
		equipo = self.kwargs['equipo']
		return Team.objects.filter(name_team=equipo)

	

class TeamList(generics.ListAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	
	def get_queryset(self):
		queryset = Team.objects.all()
		grupo = self.request.QUERY_PARAMS.get('grupo', None)

		if grupo is not None:
			queryset = queryset.filter(group_team=grupo)

		return queryset

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)