from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=200) #esme ketab
    slug = models.SlugField(unique=True)
    body = models.TextField() #darbareye ketab
    image = models.ImageField(upload_to='img') #ax ketab
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #nevisande site
    book_author = models.CharField(max_length=200) #nevisande ketab
    date_of_book = models.IntegerField() #salechap




    def __str__(self) -> str:
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
        
    
