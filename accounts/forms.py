from django import forms

from django.contrib.auth.forms import AuthenticationForm

from accounts.models import Account


class AccountLoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username', 'password']



class AccountSigninForm(forms.ModelForm):
    confirm_password = forms.CharField(
        required=True,
        #lable='Confirm password',
        widget=forms.widgets.PasswordInput() # делаем не отображаемыми вводимые симовлы
    )


    class Meta:
        model = Account
        fields = ('username', 'password', 'phone')
        widgets = {
            'password': forms.widgets.PasswordInput()           # делаем не отображаемыми вводимые симовлы
        }

    def clean_confirm_password(self):
        psd = self.cleaned_data.get('password')
        cpsd =self.cleaned_data.get('confirm_password')

        if psd and cpsd and psd != cpsd:                        # проверка на корректность ввода
            raise forms.ValidationError('Pasword and CPassowr ne sootvetstvuyut')

        return self.changed_data