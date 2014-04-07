from footballpools.models import FootballPool
from rest_framework import viewsets
from rest_framework.decorators import api_view
from footballpools.serializers import FootballPoolSerializer


# ViewSets define the view behavior.

class FootballPoolViewSet(viewsets.ModelViewSet):
    queryset = FootballPool.objects.all()
    serializer_class = FootballPoolSerializer

