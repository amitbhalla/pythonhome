#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Creating static directory..."
mkdir -p static
mkdir -p staticfiles

echo "Running migrations..."
python manage.py makemigrations core
python manage.py migrate

echo "Running collectstatic..."
python manage.py collectstatic --no-input

echo "Checking if tables exist before running seed data..."
python -c "import django; django.setup(); from django.db import connection; print('Tables exist:' if 'core_service' in connection.introspection.table_names() else 'Creating tables...')"

echo "Running seed data script..."
python seed_data.py

echo "Build complete!"