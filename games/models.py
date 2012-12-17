from django.db import models
from django.contrib.auth.models import User

class ShanghiGame(models.Model):
  name = models.CharField(max_length=100)
  done = models.BooleanField(default=False)
  num_players = models.IntegerField(default=2)
  current_round = models.IntegerField(default=10)
  current_player = models.IntegerField(default=1)
  winner = models.ForeignKey(User, related_name="shanghigames_won", null=True)

class ShanghiPlayer(models.Model):
  player_num = models.IntegerField(default=1)
  game = models.ForeignKey(ShanghiGame, related_name="players")
  player = models.ForeignKey(User, related_name="shanghigames")
  total = models.IntegerField(default=0)
  accuracy = models.DecimalField(max_digits=5, decimal_places=4, default=0)

class ShanghiRound(models.Model):
  round_number = models.IntegerField()
  singles = models.IntegerField(default=0)
  doubles = models.IntegerField(default=0)
  triples = models.IntegerField(default=0)
  shanghiplayer = models.ForeignKey(ShanghiPlayer, related_name="rounds")
