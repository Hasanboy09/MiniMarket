from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from apps.forms import RegistrationForm, LoginForm


# Create your views here.
class RegisterFormVIew(FormView):
    form_class = RegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')  # after register

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginFormVIew(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.find_user
        login(self.request, user)
        return super().form_valid(form)


class ProductListView(TemplateView):
    template_name = 'product/product-list.html'
