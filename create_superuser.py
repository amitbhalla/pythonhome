#!/usr/bin/env python
"""
Script to create a Django superuser non-interactively using environment variables.
"""
import os
import sys
import django
from django.contrib.auth import get_user_model

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amit_bhalla.settings')
django.setup()

def main():
    """Create a superuser if one doesn't exist, using environment variables."""
    # Get credentials from environment variables with defaults for username only
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    
    # Check if required environment variables are set
    if not email:
        print("Error: DJANGO_SUPERUSER_EMAIL environment variable is required.")
        return False
        
    if not password:
        print("Error: DJANGO_SUPERUSER_PASSWORD environment variable is required.")
        return False
    
    User = get_user_model()
    
    # Check if the user already exists
    if User.objects.filter(username=username).exists():
        print(f"Superuser '{username}' already exists.")
        return True
    
    # Create the superuser
    try:
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created successfully!")
        return True
    except Exception as e:
        print(f"Error creating superuser: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)