from footballpools.models import FootballPool
from rest_framework import serializers



class FootballPoolSerializer(serializers.ModelSerializer):

	user_qnl_id = serializers.Field()

	class Meta:
		model = FootballPool
		fields = ('cod_qnl','user_qnl_id','group_qnl','date_qnl','name_qnl','team_a_qnl','goals_a_qnl','team_b_qnl','goals_b_qnl','result_qnl')

#class ViewPositionSerializer(serializers.Serializer):
