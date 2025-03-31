#!/usr/bin/env python
"""
Script to fix Django migrations by marking them as applied in the database.
This is useful when migrations are out of sync with the actual database schema.
"""
import os
import sys
import django
from django.db import connection

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amit_bhalla.settings')
django.setup()

def main():
    """Fix migration records in the database."""
    print("Checking migration status...")
    
    # Check if the django_migrations table exists
    with connection.cursor() as cursor:
        cursor.execute("SELECT to_regclass('public.django_migrations')")
        table_exists = cursor.fetchone()[0]
        
        if not table_exists:
            print("Migration table doesn't exist - migrations haven't run yet.")
            return False
    
    # Check if the problematic migration is already applied
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM django_migrations WHERE app='core' AND name='0003_blogpost_field_updates'")
        migration_applied = cursor.fetchone()[0] > 0
        
        if migration_applied:
            print("Migration 0003_blogpost_field_updates is already marked as applied.")
            return True
    
    # Mark the problematic migration as applied
    print("Marking migration 0003_blogpost_field_updates as applied...")
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO django_migrations (app, name, applied) VALUES (%s, %s, NOW())",
            ['core', '0003_blogpost_field_updates']
        )
    
    print("Migration fixed successfully!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)