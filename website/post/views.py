from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

#def home (request):

#    posts=Post.objects.all()
        
#    return render(request, 'post/home.html', {'posts':posts})


class Home(ListView):
    model = Post
    template_name = 'post/home.html'
    ordering = ['-created']


def about (request):


    return render(request, 'post/about.html', {})


#def postdetail(request, pk):
#    return render (request, 'post/postdetail.html', {'posts':Post})


class PostDetail(DetailView):
    model = Post
    template_name = 'post/postdetail.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add_post.html'
    
    

class UpdatePostViews(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/update_post.html'
    #fields = ['title', 'slug', 'body']


class DeleteViews(DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    success_url = reverse_lazy('home')



class posts(ListView):
    model = Post
    template_name = 'post/homeone.html'


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'home/sign-in.html'
    success_url = reverse_lazy('login')