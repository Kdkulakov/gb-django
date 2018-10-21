from django.urls import path

from accounts.views import LoginView, SigninView

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('signin/', SigninView.as_view(), name='signin')
]