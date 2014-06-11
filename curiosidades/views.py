from curiosidades.models import Curiosidad
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from curiosidades.serializer import CuriosidadSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

# Create your views here.
class CuriosidadList(generics.ListAPIView):
	queryset = Curiosidad.objects.all()
	serializer_class = CuriosidadSerializer
	
	def get_queryset(self):
		queryset = Curiosidad.objects.all()
		ano = self.request.QUERY_PARAMS.get('ano', None)

		if ano is not None:
			queryset = queryset.filter(ano_mundial=ano)

		return queryset

class CuriosidadDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Curiosidad.objects.all()
	serializer_class = CuriosidadSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
