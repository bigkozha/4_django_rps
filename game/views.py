from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GameDetailForm, NewGameForm
from .models import Game, Move, MoveKind


@login_required
def index(request):
    # MoveKind.objects.create(name='Scissors', win_to=MoveKind.objects.create(
    #    name='Papper'), lose_to=MoveKind.objects.create(name='Stone'))
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})


@login_required
def new_game(request):
    if request.method == 'GET':
        form = NewGameForm(request.user)
        return render(request, 'new_game.html', {'form': form})

    player2 = User.objects.get(pk=int(request.POST['user']))
    instance = Game.objects.create(is_active=True, player1=request.user, player2=player2)
    return redirect('game_detail', game_id=instance.id)


@login_required
def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    form = GameDetailForm()
    moves = list(game.moves.all())

    score = []
    for x, y in zip(moves, moves[1:]):
        score.append(who_won_round(x.move_kind.name, y.move_kind.name))

    if len(moves) >= 6:
        winner_index = who_won_game(moves)
        game.is_active = False
        if winner_index != 2:
            game.winner = moves[winner_index-1].gamer
        game.save()

    if request.method == 'GET':
        return render(request, 'game_detail.html', {'form': form, 'moves': moves, 'game': game})

    if len(moves) > 0 and moves[-1].gamer == request.user:
        return redirect('error', text='same user')

    move_kind = MoveKind.objects.get(pk=int(request.POST['move_kind']))
    Move.objects.create(game=game, gamer=request.user, move_kind=move_kind)
    return redirect('game_detail', game_id=game_id)


def error(request, text):
    return render(request, 'error.html', {'text': text})


def who_won_round(move_kind1, move_kind2):
    if (move_kind1 == move_kind2):
        return 0
    if (move_kind1 == 'Papper' and move_kind2 == 'Stone'):
        return 1
    if (move_kind1 == 'Stone' and move_kind2 == 'Scissors'):
        return 1
    if (move_kind1 == 'Scissors' and move_kind2 == 'Papper'):
        return 1
    else:
        return 2


def who_won_game(moves):
    if moves.count(1) == moves.count(2):
        return 0
    if moves.count(1) > moves.count(2):
        return 1
    else:
        return 2
