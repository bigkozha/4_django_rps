from django.contrib import User
from django.db import models


class Game(models.Model):
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey(User)


class Move():
    time = models.DateField(auto_now=False, auto_now_add=True)
    game = models.ForeignKey(Game, on_delete=model.CASCADE, related_name='moves')
    gamer = models.ForeignKey(User)
