from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy

class LoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    next = reverse_lazy("")

    def form_invalid(self, form):
        form.add_error(None, "Usuário ou senha inválidos")
        return super().form_invalid(form)

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')