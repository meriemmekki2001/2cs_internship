from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages



def AccessDinied(request):
    return render(request, 'comptes/access_denied.html')


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('custom_login'))


class LoginView(FormView):
    form_class = forms.LoginForm
    success_url = reverse_lazy('core:index')
    template_name = 'comptes/login.html'

    def form_valid(self, form):
        credentials = form.cleaned_data
        user = authenticate(username=credentials['email'],
                            password=credentials['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('custom_login'))