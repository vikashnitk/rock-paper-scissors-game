from django.db import models

# Create your models here.

class Player(models.Model):
	player_name = models.CharField(max_length=200, unique=True)

class Game(models.Model):
	result = models.CharField(max_length=10)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)


class Round(models.Model):
	player_first     = models.CharField(max_length=20)
	player_second    = models.CharField(max_length=20)
	player_third     = models.CharField(max_length=20)
	computer_first   = models.CharField(max_length=20)
	computer_second  = models.CharField(max_length=20)
	computer_third   = models.CharField(max_length=20)
	player_score     = models.IntegerField()
	computer_score   = models.IntegerField()
	game             = models.ForeignKey(Game, on_delete=models.CASCADE)

