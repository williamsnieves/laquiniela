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

@csrf_exempt
@api_view(['GET', 'POST'])
def quiniela_list(request, format=None):
    if request.method == 'GET':
        quiniela  = FootballPool.objects.all()
        serializer = FootballPoolSerializer(quiniela, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FootballPoolSerializer(data=request.DATA)
        if serializer.is_valid():            
            serializer.data.user_qnl = request.user.id
            print(serializer.data.user_qnl)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
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


def pre_save(self, obj):
    obj.owner = self.request.user