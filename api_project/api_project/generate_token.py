import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")  # Replace with your project name
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def generate_token(username):
    try:
        user = User.objects.get(username=username)
        token, created = Token.objects.get_or_create(user=user)
        print(f"Token for {user.username}: {token.key}")
    except User.DoesNotExist:
        print(f"Error: User '{username}' does not exist. Please create the user first.")

if __name__ == "__main__":
    username = input("Enter the username: ")  # Prompt for username
    generate_token(username)
