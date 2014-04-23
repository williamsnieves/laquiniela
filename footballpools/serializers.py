from footballpools.models import FootballPool
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    quinielas = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'quinielas')


class FootballPoolSerializer(serializers.ModelSerializer):

	#user_qnl = serializers.RelatedField(read_only=True)
	#user_qnl = serializers.Field(source='user_qnl.username')

	class Meta:
		model = FootballPool
		fields = ('cod_qnl','user_qnl','group_qnl','date_qnl','name_qnl','team_a_qnl','goals_a_qnl','team_b_qnl','goals_b_qnl','result_qnl')

#class ViewPositionSerializer(serializers.Serializer):


