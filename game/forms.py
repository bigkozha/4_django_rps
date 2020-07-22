from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from game.models import MoveKind, Game, Move


class NewGameForm(forms.Form):
    user = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'data-test': 'player2'})) 

    def __init__(self, current_user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all().exclude(pk=current_user.pk)


class GameDetailForm(forms.Form):
    move_kind = forms.ModelChoiceField(queryset=MoveKind.objects.all(), widget=forms.Select(attrs={'data-test': 'move_kind'}))
