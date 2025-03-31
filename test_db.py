#!/usr/bin/env python
"""
Simple script to test database connection.
"""
import os
import sys
import psycopg2
from urllib.parse import urlparse

def main():
    """Test database connection"""
    print("Testing database connection...")
    
    # Get database URL from environment
    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        print("ERROR: No DATABASE_URL found in environment variables.")
        return False
    
    # Parse database URL (hide password in logs)
    safe_url = db_url.replace(
        db_url.split(':')[2].split('@')[0],
        '********'
    )
    print(f"Using database URL: {safe_url}")
    
    result = urlparse(db_url)
    
    # Extract connection details
    db_name = result.path[1:]  # Remove leading slash
    user = result.username
    password = result.password
    host = result.hostname
    port = result.port
    
    try:
        # Test connection
        print(f"Connecting to: {host}:{port}/{db_name} as {user}")
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        
        # Check tables
        with conn.cursor() as cur:
            cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public'")
            tables = [row[0] for row in cur.fetchall()]
            print(f"Database tables: {tables}")
        
        print("Database connection successful!")
        return True
        
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)