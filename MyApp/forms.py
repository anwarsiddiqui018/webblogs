from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text','image', 'tags')


class PostDeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)



class Loginform(forms.Form):
    username= forms.CharField(max_length= 500,label="Enter username")
    password= forms.CharField(label='Password', widget=forms.PasswordInput)