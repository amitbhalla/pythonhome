#!/usr/bin/env python
"""
Script to directly initialize the database tables using raw SQL statements.
This is a fallback approach when Django migrations aren't working properly.
"""
import os
import sys
import psycopg2
import django
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amit_bhalla.settings')
django.setup()

from django.conf import settings
from django.db import connection

def run_query(conn, query):
    """Run a query and print the result or error."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            print(f"Executed: {query}")
            return True
    except Exception as e:
        print(f"Error executing {query}: {e}")
        return False

def main():
    # Get database connection details from settings
    db_url = os.environ.get('DATABASE_URL', '')
    
    if not db_url:
        print("No DATABASE_URL environment variable found. Cannot continue.")
        return False
    
    # Parse the connection details from DATABASE_URL
    db_parts = db_url.split(':')
    if len(db_parts) < 4:
        print(f"Invalid DATABASE_URL format: {db_url}")
        return False
    
    try:
        db_user = db_url.split('://')[1].split(':')[0]
        db_password = db_url.split(':')[2].split('@')[0]
        db_host = db_url.split('@')[1].split(':')[0]
        db_port = db_url.split(':')[3].split('/')[0]
        db_name = db_url.split('/')[-1]
    
        print(f"Connecting to database: host={db_host}, port={db_port}, dbname={db_name}, user={db_user}")
        
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        print("Connected to database. Checking tables...")
        
        # Check if tables already exist
        with conn.cursor() as cursor:
            cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")
            tables = [row[0] for row in cursor.fetchall()]
            print(f"Existing tables: {tables}")
            
            if 'core_service' in tables:
                print("Core tables already exist. Skipping table creation.")
                return True
        
        # Create the necessary tables
        print("Creating core tables...")
        create_tables = [
            """
            CREATE TABLE core_service (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                icon_class VARCHAR(50) NOT NULL,
                short_description TEXT NOT NULL,
                full_description TEXT NOT NULL,
                order INTEGER NOT NULL,
                slug VARCHAR(100) UNIQUE NOT NULL,
                is_active BOOLEAN NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE NOT NULL
            )
            """,
            """
            CREATE TABLE core_testimonial (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                position VARCHAR(100) NOT NULL,
                company VARCHAR(100) NOT NULL,
                content TEXT NOT NULL,
                image VARCHAR(100),
                order INTEGER NOT NULL,
                is_active BOOLEAN NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE NOT NULL
            )
            """,
            """
            CREATE TABLE core_casestudy (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                slug VARCHAR(100) UNIQUE NOT NULL,
                client VARCHAR(100) NOT NULL,
                industry VARCHAR(100) NOT NULL,
                challenge TEXT NOT NULL,
                solution TEXT NOT NULL,
                results TEXT NOT NULL,
                result_metrics JSONB,
                image VARCHAR(100),
                order INTEGER NOT NULL,
                is_active BOOLEAN NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE NOT NULL
            )
            """,
            """
            CREATE TABLE core_resource (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                slug VARCHAR(100) UNIQUE NOT NULL,
                resource_type VARCHAR(20) NOT NULL,
                icon_class VARCHAR(50) NOT NULL,
                short_description TEXT NOT NULL,
                file VARCHAR(100),
                thumbnail VARCHAR(100),
                order INTEGER NOT NULL,
                is_active BOOLEAN NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE NOT NULL
            )
            """,
            """
            CREATE TABLE core_blogpost (
                id SERIAL PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                slug VARCHAR(200) UNIQUE NOT NULL,
                excerpt TEXT NOT NULL,
                content TEXT NOT NULL,
                category VARCHAR(100),
                tags VARCHAR(200),
                author VARCHAR(100) NOT NULL,
                read_time INTEGER NOT NULL,
                image VARCHAR(100),
                date DATE NOT NULL,
                is_published BOOLEAN NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE NOT NULL
            )
            """,
            """
            CREATE TABLE core_faq (
                id SERIAL PRIMARY KEY,
                question VARCHAR(200) NOT NULL,
                answer TEXT NOT NULL,
                order INTEGER NOT NULL,
                is_active BOOLEAN NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE NOT NULL
            )
            """,
            """
            CREATE TABLE core_processstep (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                icon_class VARCHAR(50) NOT NULL,
                order INTEGER NOT NULL,
                is_active BOOLEAN NOT NULL
            )
            """
        ]
        
        for table_query in create_tables:
            run_query(conn, table_query)
            
        print("Tables created successfully. Now inserting initial data...")
        
        # Insert some basic data
        service_data = """
        INSERT INTO core_service (
            title, icon_class, short_description, full_description, 
            order, slug, is_active, created_at, updated_at
        ) VALUES (
            'Marketing Strategy', 
            'fas fa-bullseye', 
            'Comprehensive marketing plans customized to your business goals, industry, and target audience to drive sustainable growth.', 
            'My marketing strategy service provides a comprehensive roadmap that aligns your marketing efforts with your business objectives.',
            1, 
            'marketing-strategy', 
            TRUE, 
            NOW(), 
            NOW()
        )
        """
        run_query(conn, service_data)
        
        print("Basic data inserted. Database initialization complete!")
        return True
            
    except Exception as e:
        print(f"Error initializing database: {e}")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)