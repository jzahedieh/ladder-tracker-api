from django.db import models


class Season(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField('Start date')
    end_date = models.DateField('End date')
    season_round = models.IntegerField()


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Ladder(models.Model):
    season = models.ForeignKey(Season)
    division = models.IntegerField()
    ladder_type = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s %s' % (self.season, self.division)


class League(models.Model):
    ladder = models.ForeignKey(Ladder, related_name='ladders')
    player = models.ForeignKey(Player, related_name='players')
    sort_order = models.IntegerField(default=0)


class Result(models.Model):
    ladder = models.ForeignKey(Ladder)
    player = models.ForeignKey(Player, related_name='result_player')
    opponent = models.ForeignKey(Player, related_name='result_opponent')
    result = models.IntegerField()
    date_added = models.DateField('Date added')
    inaccurate_flag = models.BooleanField(default=None)
