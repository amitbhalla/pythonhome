import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import importlib.util

class Command(BaseCommand):
    help = 'Setup database tables and load initial data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database setup...'))
        
        # Check if migration files exist for core app
        migration_dir = os.path.join('core', 'migrations')
        has_migrations = False
        
        if os.path.exists(migration_dir):
            if any(f.endswith('.py') and f != '__init__.py' for f in os.listdir(migration_dir)):
                has_migrations = True
                self.stdout.write(self.style.SUCCESS('Found migration files.'))
        
        # Create migrations if they don't exist
        if not has_migrations:
            self.stdout.write(self.style.WARNING('No migration files found. Creating...'))
            call_command('makemigrations', 'core', verbosity=1)
        
        # Apply migrations
        self.stdout.write(self.style.SUCCESS('Applying migrations...'))
        call_command('migrate', verbosity=1)
        
        # Check if tables were created
        with connection.cursor() as cursor:
            tables = connection.introspection.table_names()
            if 'core_service' in tables:
                self.stdout.write(self.style.SUCCESS('Database tables created successfully!'))
            else:
                self.stdout.write(self.style.ERROR('Failed to create database tables!'))
                return
        
        # Run seed data
        self.stdout.write(self.style.SUCCESS('Running seed data script...'))
        
        # Import seed_data.py and run it
        try:
            spec = importlib.util.spec_from_file_location("seed_data", "seed_data.py")
            seed_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(seed_module)
            
            # Check if create_seed_data function exists
            if hasattr(seed_module, 'create_seed_data'):
                seed_module.create_seed_data()
                self.stdout.write(self.style.SUCCESS('Seed data loaded successfully!'))
            else:
                self.stdout.write(self.style.ERROR('create_seed_data function not found in seed_data.py'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error running seed data: {e}'))
        
        self.stdout.write(self.style.SUCCESS('Database setup completed!'))