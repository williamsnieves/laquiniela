from calendars.models import Calendar
from django.shortcuts import render
from calendars.serializers import CalendarSerializer
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from calendars.serializers import CalendarSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

# Create your views here.

class CalendarList(generics.ListAPIView):
	queryset = Calendar.objects.all()
	serializer_class = CalendarSerializer

	def get_queryset(self):
		city = self.kwargs['city_match']
		return Calendar.objects.filter(city_match=city)

class CalendarDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Calendar.objects.all()
	serializer_class = CalendarSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


