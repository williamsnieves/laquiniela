from footballpools.models import FootballPool
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from footballpools.serializers import FootballPoolSerializer


# ViewSets define the view behavior.

"""class FootballPoolViewSet(viewsets.ModelViewSet):
    queryset = FootballPool.objects.all()
    serializer_class = FootballPoolSerializer"""


@api_view(['GET', 'POST'])
@csrf_exempt
def quiniela_list(request, format=None):
    if request.method == 'GET':
        quiniela  = FootballPool.objects.all()
        serializer = FootballPoolSerializer(quiniela)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FootballPoolSerializer(data = request.DATA)

        if serializer.is_valid():            
            serializer.data.user_qnl_id = request.user.id
            print(serializer.data.user_qnl_id)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def quiniela_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """              
    try:
        quiniela = FootballPool.objects.get(pk=pk)
    except FootballPool.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FootballPoolSerializer(quiniela)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FootballPoolSerializer(quiniela, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        quiniela.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

def get_queryset(self):
        queryset = FootballPool.objects.all()
        userqnl = self.request.QUERY_PARAMS.get('username', None)
        groupqnl = self.request.QUERY_PARAMS.get('group', None)

        if userqnl is not None:
            queryset = queryset.filter(user_qnl=userqnl)
        elif groupqnl is not None:
            queryset = queryset.filter(group_qnl=groupqnl)

        return queryset