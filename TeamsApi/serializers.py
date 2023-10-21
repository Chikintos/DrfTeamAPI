from urllib import response
from .models import Team,Player
from rest_framework import serializers

# player - change team +
# team - get players list
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"





class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"