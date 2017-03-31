from rest_framework import serializers
from ladder.models import Season, Player, Ladder, League, Result


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('name', 'start_date', 'end_date', 'season_round')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name')


class LadderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ladder
        fields = ('id', 'season', 'division', 'ladder_type')


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('id', 'ladder', 'player', 'sort_order')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'ladder', 'player', 'opponent', 'result', 'date_added', 'inaccurate_flag')
