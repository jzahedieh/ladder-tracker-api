from rest_framework import viewsets
from ladder.models import Season, Player, Ladder, League, Result
from ladder.serializers import SeasonSerializer, PlayerSerializer, LadderSerializer, LeagueSerializer, ResultSerializer


class SeasonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class LadderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ladder.objects.all()
    serializer_class = LadderSerializer


class LeagueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class ResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
