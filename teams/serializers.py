from teams.models import Team
from rest_framework import serializers



class TeamSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Team
        fields = ('id', 'name_team', 'country_team', 'confed_team', 'group_team','description', 'cant_titles', 'mundiales')