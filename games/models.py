from django.db import models
from django.contrib.auth.models import User

class ShanghiGame(models.Model):
  name = models.CharField(max_length=100)
  num_players = models.IntegerField(default=2)

class ShanghiPlayer(models.Model):
  player_num = models.Integer.Field()
  game = models.ForeignKey(ShanghiGame, related_name="players")
  player = models.ForeignKey(User, related_name="shangi_games")
  ten = models.IntegerField(default=0)
  eleven = models.IntegerField(default=0)
  tweleve = models.IntegerField(default=0)
  thirteen = models.IntegerField(default=0)
  fourteen = models.IntegerField(default=0)
  fifteen = models.IntegerField(default=0)
  sixteen = models.IntegerField(default=0)
  seventeen = models.IntegerField(default=0)
  eighteen = models.IntegerField(default=0)
  nineteen = models.IntegerField(default=0)
  twenty = models.IntegerField(default=0)
  bull = models.IntegerField(default=0)
