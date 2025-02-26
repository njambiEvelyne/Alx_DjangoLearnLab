from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  
from .models import Book
# Ensure this matches your user model path

class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form that includes additional fields."""
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ['username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2']
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']