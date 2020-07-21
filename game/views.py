from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import NewGameForm
from .models import Game
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def new_game(request):
    if request.method == 'GET':
        form = NewGameForm(request.user)
        return render(request, 'new_game.html', {'form': form})

    instance = Game.objects.create(is_active=True)
    return redirect('game_detail', game_id=instance.id)


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    return render(request, 'game_detail.html')
