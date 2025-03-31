#!/usr/bin/env python
"""
Script to check if seed data is loaded and load it if not.
"""
import os
import sys
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amit_bhalla.settings')
django.setup()

def main():
    """Check if seed data is loaded and load it if not."""
    from core.models import Service, Testimonial, CaseStudy, Resource, BlogPost, FAQ, ProcessStep
    from django.db import connection
    
    print("Checking if data exists...")
    
    # Check if tables exist
    with connection.cursor() as cursor:
        tables = connection.introspection.table_names()
        
        if 'core_service' not in tables:
            print("Core tables don't exist. Run migrations first.")
            return False
    
    # Check if data exists
    services_count = Service.objects.count()
    testimonials_count = Testimonial.objects.count()
    
    print(f"Found {services_count} services and {testimonials_count} testimonials.")
    
    if services_count == 0:
        print("No data found. Loading seed data...")
        
        try:
            # Try to import the seed data function directly
            from seed_data import create_seed_data
            result = create_seed_data()
            print("Seed data loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading seed data: {e}")
            return False
    else:
        print("Data already exists. Nothing to do.")
        return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)