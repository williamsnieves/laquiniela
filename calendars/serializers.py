from calendars.models import Calendar
from rest_framework import serializers



class CalendarSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Calendar
        fields = ('id', 'group_match', 'cod_match','date_match','city_match','name_match','team_a_match','goals_a_match','team_b_match','goals_b_match','result_match')





