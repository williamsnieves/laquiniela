from footballpools.models import FootballPool
from footballpoolsusers.models import FootballPoolUser
from calendars.models import Calendar
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import json

from calendars.models import ViewPosition
from footballpools.models import FootballPool, ViewPositionQnl, ViewMatchesQnl
from api.serializers import CalendarSerializer
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

# Create your views here.

@api_view(['GET'])
def positions(request):
	if request.method == 'GET':
		position = ViewPosition().getPositions()
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(position), content_type="application/json")
		#return HttpResponse(position)

@api_view(['GET'])
def group_position(request, group=""):
	if request.method == 'GET':
		position = ViewPosition().getPositionByGroup(group)
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(position), content_type="application/json")
		#return HttpResponse(position)


@api_view(['GET'])
def matches_qnl(request):
	if request.method == 'GET':
		matches_qnl = ViewMatchesQnl().getMatches()
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(matches_qnl), content_type="application/json")
		#return HttpResponse(position)


@api_view(['GET'])
def positions_qnl(request):
	if request.method == 'GET':
		position_qnl = ViewPositionQnl().getPositions()
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(position_qnl), content_type="application/json")
		#return HttpResponse(position)

@api_view(['GET'])
def group_position_qnl(request):
	if request.method == 'GET':
		group = request.REQUEST['group']
		codigo_qnl = request.REQUEST['codigoqnl']
		position_qnl = ViewPositionQnl().getPositionByGroup(group,codigo_qnl)
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(position_qnl), content_type="application/json")
		#return HttpResponse(position)


@api_view(['GET'])
def nueva_quiniela(request):
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
        quiniela = FootballPool(cod_qnl=quiniela_current.cod_qnl,user_qnl=request.user,group_qnl=item.group_match,date_qnl=item.date_match,city_match=item.city_match,flag_a_qnl=item.flag_a_match,flag_b_qnl=item.flag_b_match,name_qnl=item.name_match,team_a_qnl=item.team_a_match,goals_a_qnl=0,team_b_qnl=item.team_b_match,goals_b_qnl=0,result_qnl='0-0')
        quiniela.save()
    #return HttpResponse("creando quiniela")
    return HttpResponse(json.dumps({"success" : "true","codqnl" : quiniela_current.cod_qnl}), content_type="application/json",status=200)


@require_http_methods(["GET", "POST"])
@csrf_exempt
def quiniela(request):
	if request.method == 'POST':
		#print(request.POST)
		grupo = request.REQUEST['grupo']
		codigo_qnl = request.REQUEST['codigo']
		user = request.user

		datos = json.loads(request.body.decode())
		if not datos:
			return HttpResponse(json.dumps({"error" : "no existen datos"}), content_type="application/json",status=400)

		#quiniela = serializers.deserialize('json',FootballPool.objects.filter(group_qnl=grupo).filter(cod_qnl=codigo_qnl).filter(user_qnl=user).update(goals_a_qnl=3,goals_b_qnl=2))
		result = datos['goles_a'] + "-" + datos['goles_b']
		try:
			FootballPool.objects.filter(group_qnl=grupo).filter(cod_qnl=codigo_qnl).filter(user_qnl=user).update(goals_a_qnl=datos['goles_a'],goals_b_qnl=datos['goles_b'],result_qnl=result)
			return HttpResponse(json.dumps({"success" : "true"}), content_type="application/json",status=200)
		except FootballPool.DoesNotExist:
			raise Http404
			return HttpResponse(json.dumps({"error" : "error"}), content_type="application/json",status=404)
		except DatabaseError as e:
			return HttpResponse(json.dumps({"error" : "database-error"}), content_type="application/json")
			#return HttpResponse(json.dumps({"error" : "error"}), content_type="application/json",status=404)


	if request.method == 'GET':
		grupo = request.GET.get('grupo')
		codigo_qnl = request.GET.get('codigo')
		user = request.user
		if not grupo:
			quiniela  = serializers.serialize('json',FootballPool.objects.all())
		else:
			quiniela = serializers.serialize('json',FootballPool.objects.filter(group_qnl=grupo).filter(cod_qnl=codigo_qnl).filter(user_qnl=user))		
		
		return HttpResponse(quiniela)
		#return HttpResponse(request.GET.get('prueba'))
	



