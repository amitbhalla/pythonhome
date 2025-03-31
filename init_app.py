#!/usr/bin/env python
"""
Direct database initialization script - fixed version.
This script connects to the database and creates all necessary tables
when Django migrations might be failing.
"""
import os
import sys
import psycopg2
import django
from urllib.parse import urlparse

def main():
    """Main function to initialize the database."""
    print("Starting direct database initialization...")
    
    # Get database URL from environment
    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        print("ERROR: No DATABASE_URL found in environment variables.")
        return False
    
    # Parse database URL
    print(f"Parsing database URL: {db_url.split('@')[0].split('//')[0]}//****@{db_url.split('@')[1]}")
    result = urlparse(db_url)
    
    # Extract connection details
    db_name = result.path[1:]  # Remove leading slash
    user = result.username
    password = result.password
    host = result.hostname
    port = result.port
    
    print(f"Connecting to: {host}:{port}/{db_name} as {user}")
    
    try:
        # Connect to database
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.autocommit = True
        
        # Check if tables exist
        with conn.cursor() as cur:
            cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public'")
            tables = [row[0] for row in cur.fetchall()]
            print(f"Existing tables: {tables}")
            
            if 'core_service' in tables:
                print("Database tables already exist. Nothing to do.")
                return True
        
        # If we get here, tables don't exist
        print("Creating database tables manually...")
        
        # Create basic tables needed for the app to work
        with conn.cursor() as cur:
            # Create core_service table - using the proper PostgreSQL keyword for order
            cur.execute("""
                CREATE TABLE core_service (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100) NOT NULL,
                    icon_class VARCHAR(50) NOT NULL,
                    short_description TEXT NOT NULL,
                    full_description TEXT NOT NULL DEFAULT '',
                    "order" INTEGER NOT NULL,
                    slug VARCHAR(100) UNIQUE NOT NULL,
                    is_active BOOLEAN NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                    updated_at TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)
            
            # Insert a sample service
            cur.execute("""
                INSERT INTO core_service (
                    title, icon_class, short_description, full_description,
                    "order", slug, is_active, created_at, updated_at
                ) VALUES (
                    'Marketing Strategy',
                    'fas fa-bullseye',
                    'Comprehensive marketing plans customized to your business goals.',
                    'My marketing strategy service provides a comprehensive roadmap.',
                    1,
                    'marketing-strategy',
                    TRUE,
                    NOW(),
                    NOW()
                )
            """)
            
            print("Basic database tables created.")
            return True
            
    except Exception as e:
        print(f"ERROR during database initialization: {e}")
        return False
        
if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)