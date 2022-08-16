from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from post.models import Post









from django.shortcuts import render, redirect
from django.contrib.auth import authenticate #login
from .forms import LoginForm, SignUpForm



class UserLoginView(generic.CreateView):
    form_class = LoginForm
    template_name = 'registration/sign-in.html'
    success_url = reverse_lazy('login')


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign-up.html'
    
class UserPostDetail(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'registration/userpost.html'

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
