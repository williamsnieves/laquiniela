from curiosidades.models import Curiosidad
from rest_framework import serializers



class CuriosidadSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Curiosidad
        fields = ('id', 'cod_mundial', 'copa','ano_mundial','pais_sede','cant_equipos','cant_partidos','cant_goles','promedio_goles','campeon','subcampeon','tercero','cuarto','goleadores','max_goles','balon_oro','fairplay','descripcion','curiosidad')