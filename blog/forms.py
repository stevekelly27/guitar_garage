from .models import Comment, Post, Catagory
from django import forms
from django_summernote.widgets import SummernoteWidget


choices = Catagory.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'catagory', 'featured_image', 'excerpt', 'content')
        widgets = {
            'catagory': forms.Select(
                choices=choice_list, attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
        }
