Features
User Registration
User Login & Logout
Profile Management
Secure Password Handling
CSRF Protection

pip install django
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate    # For Windows

This is the appearence of the settings file where I've included the installed app
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Ensure the blog app is listed
]

AUTH_USER_MODEL = 'blog.CustomUser'  # If using a custom user model
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

python manage.py makemigrations blog
python manage.py migrate

from django.urls import path
from .views import register_view, login_view, logout_view, profile_view
from django.contrib.auth import views as auth_views


configuration of the urls
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
]
