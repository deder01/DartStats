from django.db import models

class ShanghiGame(models.Model):
  n =  models.IntegerField()

class ShanghiPlayer(models.Model):
  headline = models.CharField(max_length=100)
  game = models.ForeignKey(ShanghiGame)
