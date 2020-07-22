from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import NewGameForm, GameDetailForm
from .models import Game, MoveKind, Move

def index(request): 
    return render(request, 'index.html')


def new_game(request):
    if request.method == 'GET':
        form = NewGameForm(request.user)
        return render(request, 'new_game.html', {'form': form})

    instance = Game.objects.create(is_active=True)
    return redirect('game_detail', game_id=instance.id)

@login_required
def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    form = GameDetailForm()
    moves = game.moves.all()
    if request.method == 'GET':
        return render(request, 'game_detail.html', {'form': form})

    Move.objects.create(game=game,gamer=request.user) 
    return render(request, 'game_detail.html', {'form': form, 'moves':moves })
