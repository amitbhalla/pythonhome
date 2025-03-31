from django.http import HttpResponse
from django.db import connection
from django.conf import settings
import os
import sys
import django

def debug_info(request):
    """View to provide diagnostic information"""
    if not settings.DEBUG:
        return HttpResponse("Debug mode is disabled. Set DEBUG=True to see information.")
    
    response_parts = []
    
    # Basic environment info
    response_parts.append("<h1>Django Debug Information</h1>")
    response_parts.append(f"<p>Python version: {sys.version}</p>")
    response_parts.append(f"<p>Django version: {django.__version__}</p>")  # Fixed this line
    response_parts.append(f"<p>Running on: {os.uname().nodename}</p>")
    
    # Database connection info
    response_parts.append("<h2>Database Information</h2>")
    db_name = settings.DATABASES['default'].get('NAME', 'Unknown')
    response_parts.append(f"<p>Database name: {db_name}</p>")
    
    # Check database tables
    response_parts.append("<h2>Database Tables</h2>")
    try:
        with connection.cursor() as cursor:
            tables = connection.introspection.table_names()
            if tables:
                response_parts.append("<ul>")
                for table in tables:
                    response_parts.append(f"<li>{table}</li>")
                response_parts.append("</ul>")
            else:
                response_parts.append("<p>No tables found in database!</p>")
    except Exception as e:
        response_parts.append(f"<p>Error checking tables: {e}</p>")
    
    # Installed apps
    response_parts.append("<h2>Installed Apps</h2>")
    response_parts.append("<ul>")
    for app in settings.INSTALLED_APPS:
        response_parts.append(f"<li>{app}</li>")
    response_parts.append("</ul>")
    
    # Migration files
    response_parts.append("<h2>Migration Files</h2>")
    migration_dir = os.path.join(settings.BASE_DIR, 'core', 'migrations')
    response_parts.append(f"<p>Migration directory: {migration_dir}</p>")
    if os.path.exists(migration_dir):
        files = os.listdir(migration_dir)
        if files:
            response_parts.append("<ul>")
            for filename in files:
                if filename.endswith('.py'):
                    response_parts.append(f"<li>{filename}</li>")
            response_parts.append("</ul>")
        else:
            response_parts.append("<p>No migration files found!</p>")
    else:
        response_parts.append("<p>Migration directory does not exist!</p>")
    
    # Environment variables
    response_parts.append("<h2>Environment Variables</h2>")
    response_parts.append("<ul>")
    for key, value in os.environ.items():
        if key.startswith('DJANGO') or key in ['DATABASE_URL', 'DEBUG', 'RENDER']:
            # Mask sensitive values
            if 'SECRET' in key or 'PASSWORD' in key or 'URL' in key:
                value = '*****'
            response_parts.append(f"<li>{key}: {value}</li>")
    response_parts.append("</ul>")
    
    return HttpResponse("".join(response_parts))