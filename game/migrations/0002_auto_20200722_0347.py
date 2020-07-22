# Generated by Django 3.0.8 on 2020-07-22 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_player1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='player2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_player2', to=settings.AUTH_USER_MODEL),
        ),
    ]
