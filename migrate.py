#!/usr/bin/env python
"""
Script to manually run migrations and seed data.
Run this script directly to initialize the database.
"""
import os
import sys
import django
from django.core.management import call_command

def main():
    print("Setting up environment...")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amit_bhalla.settings")
    django.setup()
    
    print("Creating migrations...")
    try:
        call_command('makemigrations', 'core')
    except Exception as e:
        print(f"Error creating migrations: {e}")
    
    print("Applying migrations...")
    try:
        call_command('migrate')
    except Exception as e:
        print(f"Error applying migrations: {e}")
        
    print("Loading initial data...")
    try:
        from seed_data import create_seed_data
        create_seed_data()
    except Exception as e:
        print(f"Error loading seed data: {e}")
    
    print("Done! Database should be initialized.")

if __name__ == "__main__":
    main()