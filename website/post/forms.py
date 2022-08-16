from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'slug', 'body', 'book_author', 'date_of_book', 'author' )
        widget = {
            'title':forms.TextInput(attrs={'class':'form-conrtol'}),
            'slug':forms.TextInput(attrs={'class':'form-conrtol'}),
            'body':forms.Textarea(attrs={'class':'form-conrtol'}),
            'author':forms.Select(attrs={'class':'form-conrtol'}),
            'book_author':forms.Select(attrs={'class':'form-conrtol'}),
            'date_of_book':forms.Select(attrs={'class':'form-conrtol'}),}
        
        
