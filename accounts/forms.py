from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import Account


class AccountLoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username', 'password']

