from .serializers import TeamSerializer, PlayerSerializer
from rest_framework.viewsets import generics
from .models import Team, Player
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(methods=['get'], detail=True)
    def getplayers(self, request, pk=None):
        # Get the team object associated with the request
        team = self.get_object()
        try:
            # Filter players by the team
            players = Player.objects.filter(team=team)
            return Response({'players': players.values()})
        except Team.DoesNotExist:
            return Response({'error': 'Team not found'}, status=400)

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(methods=['post'], detail=True)
    def changeteam(self, request, pk=None):
        # Get the player object associated with the request
        player = self.get_object()
        team = request.data.get('pk')
        try:
            team = Team.objects.get(pk=team) # Get the team object based on the provided pk
            
            player.team = team # Change the team of the player and save
            player.save()
            return Response({'user': player.id, 'team': team.id})
        except Team.DoesNotExist:
            return Response({'error': 'Team not found'}, status=400)
