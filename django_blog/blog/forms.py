from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Tag
from .models import Comment
from taggit.forms import TagWidget



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Write a comment...'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas.")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        tag_names = self.cleaned_data.get('tags', '').split(',')
        tags = [Tag.objects.get_or_create(name=tag.strip())[0] for tag in tag_names if tag.strip()]
        return tags
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Ensure 'tags' is included
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control'}),  # Add TagWidget
        }