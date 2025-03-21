from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget  # Import TagWidget
from .models import Post, Comment


# User Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Profile Edit Form
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


# Post Form with Tags
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control'}),  # Use TagWidget for tag input
        }


# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Write a comment...'})
        }
