from django.shortcuts import render, redirect
from django.views.generic import FormView
from accounts.models import Account
from accounts.forms import AccountLoginForm, AccountSigninForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from accounts.mixins import AnonRequiredMixin


class LoginView(AnonRequiredMixin, FormView):
    model = Account
    form_class = AccountLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('products:list')
    redirect_url = reverse_lazy('products:list')

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



class SigninView(AnonRequiredMixin, FormView):
    model = Account
    form_class = AccountSigninForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('products:list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True

            password = request.POST.get("password")
            user.set_password(password)
            user.save()


            login(request, user)

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})
