from footballpools.models import FootballPool
from footballpoolsusers.models import FootballPoolUser
from knockout.models import Knockout, ViewOctavos
from quarter.models import Quarter,  ViewCuartos
from semifinal.models import Semifinal, ViewSemis
from final.models import Final, ViewFinal
from invitations.models import Invitation
from django.db import models, connection
from calendars.models import Calendar
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import json
from django.core.mail import send_mail
from calendars.models import ViewPosition
from footballpools.models import FootballPool, ViewPositionQnl, ViewMatchesQnl
from api.serializers import CalendarSerializer
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

# Create your views here.

@api_view(['GET'])
def get_quinielas(request):
	if request.method == 'GET':
		quinielas = FootballPoolUser.objects.filter(username=request.user)
		#return Response(position)
		jsonResponse = serializers.serialize("json", quinielas)
		return HttpResponse(jsonResponse, content_type="application/json")
		#return HttpResponse(position)

@api_view(['GET'])
def positions(request):
	if request.method == 'GET':
		position = ViewPosition().getPositions()
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(position), content_type="application/json")
		#return HttpResponse(position)

@api_view(['GET'])
def invitations(request):
	if request.method == 'GET':
		cant = Invitation.objects.filter(username=request.user).filter(invitacion=1).count()
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps({"cant" : cant}), content_type="application/json",status=200)
		#return HttpResponse(position)

@require_http_methods(["GET", "POST"])
@csrf_exempt
def invitations_save(request):
	if request.method == 'POST':
		datos = json.loads(request.body.decode())

		invitacion = Invitation(username=request.user,invitacion=datos['data']['invitacion'])
		print(datos['data']['invitados'][0]['email'])
		invitacion.save()

		contenido = "Tu amigo "+request.user.first_name+" "+request.user.last_name+" te ha invitado a jugar la quiniela del mundial"
		contenido+= "en http://www.futbolgamb.com no dejes de entrar y divertirte tratando de asertar los resultados de los partidos y compitiendo contra otros"
		correos = []	

		for email in datos['data']['invitados']:
			correos.append(email['email'])

		send_mail('Invitaciones para futbolgamb', contenido, 'from@example.com',correos, fail_silently=False)
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps({"success" : "true"}), content_type="application/json",status=200)
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

@api_view(['GET'])
def octavos_qnl(request):
	if request.method == 'GET':
		codigo_qnl = request.REQUEST['codigoqnl']
		partidos_octavos_qnl = ViewOctavos().getMatchesOctavos(codigo_qnl)
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(partidos_octavos_qnl), content_type="application/json")
		#return HttpResponse(position)

@api_view(['GET'])
def cuartos_qnl(request):
	if request.method == 'GET':
		codigo_qnl = request.REQUEST['codigoqnl']
		partidos_cuartos_qnl = ViewCuartos().getMatchesCuartos(codigo_qnl)
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(partidos_cuartos_qnl), content_type="application/json")
		#return HttpResponse(position)

@api_view(['GET'])
def semis_qnl(request):
	if request.method == 'GET':
		codigo_qnl = request.REQUEST['codigoqnl']
		partidos_semis_qnl = ViewSemis().getMatchesSemis(codigo_qnl)
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(partidos_semis_qnl), content_type="application/json")
		#return HttpResponse(position)

@api_view(['GET'])
def final_qnl(request):
	if request.method == 'GET':
		codigo_qnl = request.REQUEST['codigoqnl']
		partidos_final_qnl = ViewFinal().getMatchesFinal(codigo_qnl)
		#return Response(position)
		#jsonResponse = serializers.serialize("json", position)
		return HttpResponse(json.dumps(partidos_final_qnl), content_type="application/json")
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
        quiniela = FootballPool(cod_qnl=quiniela_current.cod_qnl,user_qnl=request.user,group_qnl=item.group_match,date_qnl=item.date_match,city_match=item.city_match,flag_a_qnl=item.flag_a_match,flag_b_qnl=item.flag_b_match,name_qnl=item.name_match,team_a_qnl=item.team_a_match,goals_a_qnl=0,team_b_qnl=item.team_b_match,goals_b_qnl=0,result_qnl='0-0',order_qnl=item.order_match)
        quiniela.save()
    
    partido1_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8A',cod_equipo='1A',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido2_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8A',cod_equipo='2B',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido3_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8B',cod_equipo='1C',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido4_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8B',cod_equipo='2D',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido5_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8C',cod_equipo='1B',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido6_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8C',cod_equipo='2A',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido7_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8D',cod_equipo='1D',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido8_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8D',cod_equipo='2C',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido9_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8E',cod_equipo='1E',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido10_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8E',cod_equipo='2F',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido11_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8F',cod_equipo='1G',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido12_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8F',cod_equipo='2H',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido13_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8G',cod_equipo='1F',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido14_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8G',cod_equipo='2E',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido15_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8H',cod_equipo='1H',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')
    partido16_octavos = Knockout(cod_qnl=quiniela_current.cod_qnl,cod_juego='8H',cod_equipo='2G',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_octavos='')

    partido1_octavos.save()
    partido2_octavos.save()
    partido3_octavos.save()
    partido4_octavos.save()
    partido5_octavos.save()
    partido6_octavos.save()
    partido7_octavos.save()
    partido8_octavos.save()
    partido9_octavos.save()
    partido10_octavos.save()
    partido11_octavos.save()
    partido12_octavos.save()
    partido13_octavos.save()
    partido14_octavos.save()
    partido15_octavos.save()
    partido16_octavos.save()

    partido1_cuartos = Quarter(cod_qnl=quiniela_current.cod_qnl,cod_juego='4A',cod_equipo='8A',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_cuartos='')
    partido2_cuartos = Quarter(cod_qnl=quiniela_current.cod_qnl,cod_juego='4A',cod_equipo='8B',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_cuartos='')
    partido3_cuartos = Quarter(cod_qnl=quiniela_current.cod_qnl,cod_juego='4B',cod_equipo='8C',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_cuartos='')
    partido4_cuartos = Quarter(cod_qnl=quiniela_current.cod_qnl,cod_juego='4B',cod_equipo='8D',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_cuartos='')
    partido5_cuartos = Quarter(cod_qnl=quiniela_current.cod_qnl,cod_juego='4C',cod_equipo='8E',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_cuartos='')
    partido6_cuartos = Quarter(cod_qnl=quiniela_current.cod_qnl,cod_juego='4C',cod_equipo='8F',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_cuartos='')
    partido7_cuartos = Quarter(cod_qnl=quiniela_current.cod_qnl,cod_juego='4D',cod_equipo='8G',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_cuartos='')
    partido8_cuartos = Quarter(cod_qnl=quiniela_current.cod_qnl,cod_juego='4D',cod_equipo='8H',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_cuartos='')

    partido1_cuartos.save()
    partido2_cuartos.save()
    partido3_cuartos.save()
    partido4_cuartos.save()
    partido5_cuartos.save()
    partido6_cuartos.save()
    partido7_cuartos.save()
    partido8_cuartos.save()

    partido1_semis = Semifinal(cod_qnl=quiniela_current.cod_qnl,cod_juego='SFA',cod_equipo='4A',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_semis='')
    partido2_semis = Semifinal(cod_qnl=quiniela_current.cod_qnl,cod_juego='SFA',cod_equipo='4B',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_semis='')
    partido3_semis = Semifinal(cod_qnl=quiniela_current.cod_qnl,cod_juego='SFB',cod_equipo='4C',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_semis='')
    partido4_semis = Semifinal(cod_qnl=quiniela_current.cod_qnl,cod_juego='SFB',cod_equipo='4D',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_semis='')

    partido1_semis.save()
    partido2_semis.save()
    partido3_semis.save()
    partido4_semis.save()

    partido1_final = Final(cod_qnl=quiniela_current.cod_qnl,cod_juego='FIN',cod_equipo='SFA',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_final='')
    partido2_final = Final(cod_qnl=quiniela_current.cod_qnl,cod_juego='FIN',cod_equipo='SFB',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_final='')
    partido3_final = Final(cod_qnl=quiniela_current.cod_qnl,cod_juego='34L',cod_equipo='PSA',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_final='')
    partido4_final = Final(cod_qnl=quiniela_current.cod_qnl,cod_juego='34l',cod_equipo='PSB',equipo='EQP',goles=0,clasificado='NA',puntuacion=0,ruta='',progress_final='')

    partido1_final.save()
    partido2_final.save()
    partido3_final.save()
    partido4_final.save()

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
		#result = datos['data']['goles_a'] + "-" + datos['goles_b']

		for data in datos['data']:
			result = data['goles_a'] + "-" + data['goles_b']			
			responseqnl = FootballPool.objects.filter(group_qnl=grupo).filter(cod_qnl=codigo_qnl).filter(user_qnl=user).filter(order_qnl=data['partido']).update(goals_a_qnl=data['goles_a'],goals_b_qnl=data['goles_b'],progress_qnl=data['progress'],result_qnl=result)
		
		#updateOctavos = Knockout.filter(cod_qnl=codigo_qnl).update()

		cursor = connection.cursor()
		cursor.execute("UPDATE knockout_knockout SET cod_qnl = '"+codigo_qnl+"',equipo=vw_octavos_qnl.team FROM vw_octavos_qnl WHERE vw_octavos_qnl.cod_qnl=knockout_knockout.cod_qnl AND  vw_octavos_qnl.clas1 = knockout_knockout.cod_equipo")

		return HttpResponse(json.dumps({"success" : "true"}), content_type="application/json",status=200)

@require_http_methods(["GET", "POST"])
@csrf_exempt
def octavos_update(request):
	if request.method == 'POST':
		codigo_qnl = request.REQUEST['codigoqnl']
		datos = json.loads(request.body.decode())

		if not datos:
			return HttpResponse(json.dumps({"error" : "no existen datos"}), content_type="application/json",status=400)

		#quiniela = serializers.deserialize('json',FootballPool.objects.filter(group_qnl=grupo).filter(cod_qnl=codigo_qnl).filter(user_qnl=user).update(goals_a_qnl=3,goals_b_qnl=2))
		#result = datos['data']['goles_a'] + "-" + datos['goles_b']

		for data in datos['data']:			
			responseqnl = Knockout.objects.filter(cod_qnl=codigo_qnl).filter(cod_equipo=data['partido']).update(goles=data['goles'],progress_octavos=data['progress'])

		cursor = connection.cursor()
		cursor.execute("UPDATE quarter_quarter SET cod_qnl ='"+codigo_qnl+"',equipo=vw_cuartos_qnl.equipo FROM vw_cuartos_qnl WHERE vw_cuartos_qnl.cod_qnl=quarter_quarter.cod_qnl AND vw_cuartos_qnl.cod_juego = quarter_quarter.cod_equipo")
		
		return HttpResponse(json.dumps({"success" : "true"}), content_type="application/json",status=200)

@require_http_methods(["GET", "POST"])
@csrf_exempt
def cuartos_update(request):
	if request.method == 'POST':
		codigo_qnl = request.REQUEST['codigoqnl']
		datos = json.loads(request.body.decode())

		if not datos:
			return HttpResponse(json.dumps({"error" : "no existen datos"}), content_type="application/json",status=400)

		#quiniela = serializers.deserialize('json',FootballPool.objects.filter(group_qnl=grupo).filter(cod_qnl=codigo_qnl).filter(user_qnl=user).update(goals_a_qnl=3,goals_b_qnl=2))
		#result = datos['data']['goles_a'] + "-" + datos['goles_b']

		for data in datos['data']:			
			responseqnl = Quarter.objects.filter(cod_qnl=codigo_qnl).filter(cod_equipo=data['partido']).update(goles=data['goles'],progress_cuartos=data['progress'])

		cursor = connection.cursor()
		cursor.execute("UPDATE semifinal_semifinal SET cod_qnl ='"+codigo_qnl+"',equipo=vw_semifinal_qnl.equipo FROM vw_semifinal_qnl WHERE vw_semifinal_qnl.cod_qnl=semifinal_semifinal.cod_qnl AND vw_semifinal_qnl.cod_juego = semifinal_semifinal.cod_equipo")
		
		return HttpResponse(json.dumps({"success" : "true"}), content_type="application/json",status=200)

@require_http_methods(["GET", "POST"])
@csrf_exempt
def semifinal_update(request):
	if request.method == 'POST':
		codigo_qnl = request.REQUEST['codigoqnl']
		datos = json.loads(request.body.decode())

		if not datos:
			return HttpResponse(json.dumps({"error" : "no existen datos"}), content_type="application/json",status=400)

		#quiniela = serializers.deserialize('json',FootballPool.objects.filter(group_qnl=grupo).filter(cod_qnl=codigo_qnl).filter(user_qnl=user).update(goals_a_qnl=3,goals_b_qnl=2))
		#result = datos['data']['goles_a'] + "-" + datos['goles_b']

		for data in datos['data']:			
			responseqnl = Semifinal.objects.filter(cod_qnl=codigo_qnl).filter(cod_equipo=data['partido']).update(goles=data['goles'],progress_semis=data['progress'])

		cursor = connection.cursor()
		cursor.execute("UPDATE final_final SET cod_qnl ='"+codigo_qnl+"',equipo=vw_final_qnl.equipo FROM vw_final_qnl WHERE vw_final_qnl.cod_qnl=final_final.cod_qnl AND vw_final_qnl.cod_juego = final_final.cod_equipo")
		
		return HttpResponse(json.dumps({"success" : "true"}), content_type="application/json",status=200)

@require_http_methods(["GET", "POST"])
@csrf_exempt
def final_update(request):
	if request.method == 'POST':
		codigo_qnl = request.REQUEST['codigoqnl']
		datos = json.loads(request.body.decode())

		if not datos:
			return HttpResponse(json.dumps({"error" : "no existen datos"}), content_type="application/json",status=400)

		#quiniela = serializers.deserialize('json',FootballPool.objects.filter(group_qnl=grupo).filter(cod_qnl=codigo_qnl).filter(user_qnl=user).update(goals_a_qnl=3,goals_b_qnl=2))
		#result = datos['data']['goles_a'] + "-" + datos['goles_b']

		for data in datos['data']:			
			responseqnl = Final.objects.filter(cod_qnl=codigo_qnl).filter(cod_equipo=data['partido']).update(goles=data['goles'],progress_final=data['progress'])

		
		return HttpResponse(json.dumps({"success" : "true"}), content_type="application/json",status=200)

@api_view(['GET'])
def get_totalqnl(request):
	if request.method == "GET":
		codigoqnl = request.REQUEST['codigo']
		#codigoqnl = "1williams.nieves.71"
		cant = FootballPoolUser.objects.filter(cod_qnl=codigoqnl).count()

		return HttpResponse(json.dumps({"cant" : cant}), content_type="application/json",status=200)

@api_view(['GET'])
def get_progressqnl(request):
	if request.method == "GET":
		codigoqnl = request.REQUEST['codigo']
		#codigoqnl = "1williams.nieves.71"
		cant = FootballPool.objects.filter(cod_qnl=codigoqnl).filter(progress_qnl=True).count()

		return HttpResponse(json.dumps({"cant" : cant}), content_type="application/json",status=200)

@api_view(['GET'])
def get_progressoctavos_qnl(request):
	if request.method == "GET":
		codigoqnl = request.REQUEST['codigo']
		#codigoqnl = "1williams.nieves.71"
		cant = Knockout.objects.filter(cod_qnl=codigoqnl).filter(progress_octavos=True).count()

		return HttpResponse(json.dumps({"cant" : cant}), content_type="application/json",status=200)

@api_view(['GET'])
def get_progresscuartos_qnl(request):
	if request.method == "GET":
		codigoqnl = request.REQUEST['codigo']
		#codigoqnl = "1williams.nieves.71"
		cant = Quarter.objects.filter(cod_qnl=codigoqnl).filter(progress_cuartos=True).count()

		return HttpResponse(json.dumps({"cant" : cant}), content_type="application/json",status=200)

@api_view(['GET'])
def get_progresssemis_qnl(request):
	if request.method == "GET":
		codigoqnl = request.REQUEST['codigo']
		#codigoqnl = "1williams.nieves.71"
		cant = Semifinal.objects.filter(cod_qnl=codigoqnl).filter(progress_semis=True).count()

		return HttpResponse(json.dumps({"cant" : cant}), content_type="application/json",status=200)

@api_view(['GET'])
def get_progressfinal_qnl(request):
	if request.method == "GET":
		codigoqnl = request.REQUEST['codigo']
		#codigoqnl = "1williams.nieves.71"
		cant = Final.objects.filter(cod_qnl=codigoqnl).filter(progress_final=True).count()

		return HttpResponse(json.dumps({"cant" : cant}), content_type="application/json",status=200)

@api_view(['GET'])
def get_completefaseqnl(request):
	if request.method == "GET":
		codigoqnl = request.REQUEST['codigo']
		#codigoqnl = "1williams.nieves.71"
		cant = FootballPoolUser.objects.filter(cod_qnl=codigoqnl).filter(qnl_fase=1).count()
		
		return HttpResponse(json.dumps({"cant" : cant}), content_type="application/json",status=200)

@api_view(['GET'])
def get_eliminatoria(request):
	if request.method == "GET":
		codigoqnl = request.REQUEST['codigo']
		#codigoqnl = "1williams.nieves.71"
		cant = FootballPoolUser.objects.filter(cod_qnl=codigoqnl).filter(qnl_eliminatoria=1).count()
		
		return HttpResponse(json.dumps({"cant" : cant}), content_type="application/json",status=200)


@api_view(['GET'])
def get_validqnl(request):
	if request.method == "GET":
		codigoqnl = request.REQUEST['codigo']
		#codigoqnl = "1williams.nieves.71"
		codigo = FootballPoolUser.objects.filter(cod_qnl=codigoqnl)

		if not codigo:
			return HttpResponse(json.dumps({"success" : False}), content_type="application/json",status=200)
		else:				
			return HttpResponse(json.dumps({"codigo" : codigo[0].cod_qnl, "success" : True}), content_type="application/json",status=200)



			
	



