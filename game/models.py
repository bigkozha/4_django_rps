from django.conf import settings
from django.db import models


class Game(models.Model):
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    player1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                null=True, related_name='game_player1')
    player2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                null=True, related_name='game_player2')


class Move(models.Model):
    time = models.DateField(auto_now=False, auto_now_add=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='moves')
    gamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    move_kind = models.ForeignKey('MoveKind', on_delete=models.DO_NOTHING)


class MoveKind(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
