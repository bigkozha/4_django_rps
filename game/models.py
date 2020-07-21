from django.conf import settings
from django.db import models


class Game(models.Model):
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Move():
    time = models.DateField(auto_now=False, auto_now_add=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='moves')
    gamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
