from django.db import models


class Game(models.Model):
    is_active = models.BooleanField(default=True)