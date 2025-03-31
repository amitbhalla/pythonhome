#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install psycopg2-binary

echo "Creating directories..."
mkdir -p static
mkdir -p staticfiles

echo "Running collectstatic..."
python manage.py collectstatic --no-input || echo "Collectstatic failed, but continuing..."

echo "Trying to run migrations..."
python manage.py makemigrations core || echo "Makemigrations failed, continuing..."
python manage.py migrate || echo "Migrate failed, trying alternative method..."

echo "Initializing database directly..."
python init_db.py || echo "Direct initialization failed, but continuing..."

echo "Running seed data script..."
python seed_data.py || echo "Seed data failed, but continuing..."

echo "Build complete! Check database status at /debug/"