from django import forms
from django.conf import settings
from django.contrib.auth.models import User


class NewGameForm(forms.Form):
    user = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'data-test': 'player2'}))

    def __init__(self, current_user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all().exclude(pk=current_user.pk)
