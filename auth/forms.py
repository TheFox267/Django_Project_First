from django import forms
from django.contrib.auth.models import User


class RegForm(forms.ModelForm):
    reg = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

#  Copyright (c) 2020.  Designed TheFox https://github.com/TheFox267
