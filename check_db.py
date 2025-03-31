#!/usr/bin/env python
import os
import sys
import django
from django.db import connection

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amit_bhalla.settings')
django.setup()

# Check database connection and tables
try:
    with connection.cursor() as cursor:
        tables = connection.introspection.table_names()
        print(f"Connected to database successfully!")
        print(f"Database contains {len(tables)} tables:")
        for table in tables:
            print(f" - {table}")
        
        if not tables:
            print("\nNo tables found. Migrations may not have run correctly.")
        else:
            print("\nDatabase setup looks good!")
except Exception as e:
    print(f"Database connection error: {e}")
    sys.exit(1)