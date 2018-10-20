from django.shortcuts import render, redirect
from django.views.generic import FormView
from accounts.models import Account
from accounts.forms import AccountLoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


class LoginView(FormView):
    model = Account
    form_class = AccountLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('products:list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            usr = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(
                username=usr,
                password=pwd
            )

            if user and user.is_active:
                login(request, user)
                return redirect(self.success_url)


            return render(
                request,
                self.template_name,
                {'form': form}
            )
