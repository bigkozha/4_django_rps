from django.shortcuts import render, reverse
from .forms import NewGameForm


def index(request):
    return render(request, 'index.html')


def new_game(request):
    form = NewGameForm()

    context = {
        'form': form
    }

    return render(request, 'new_game.html', context)
