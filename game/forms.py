from django import forms
from django.conf import settings
from django.contrib.auth.models import User


class NewGameForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'data-test' : 'player2'}))
