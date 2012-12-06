from django.db import models
from django.contrib.auth.models import User

class ShanghiGame(models.Model):
  name = models.CharField(max_length=100)
  done = models.BooleanField(default="false")
  num_players = models.IntegerField(default=2)
  current_round = models.IntegerField(default=10)
  current_player = models.IntegerField(default=2)

class ShanghiPlayer(models.Model):
  player_num = models.IntegerField(default=1)
  game = models.ForeignKey(ShanghiGame, related_name="players")
  player = models.ForeignKey(User, related_name="shangi_games")

class ShanghiRound(models.Model):
  round_number = models.IntegerField()
  number_of_darts = models.IntegerField()
  number_of_hits = models.IntegerField()
  shanghiplayer = models.ForeignKey(ShanghiPlayer, related_name="rounds")
