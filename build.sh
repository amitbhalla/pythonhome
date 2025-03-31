#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Creating directories..."
mkdir -p static
mkdir -p staticfiles

echo "Setting up database (Method 1: Django command)..."
python manage.py makemigrations core || echo "Makemigrations failed, continuing..."
python manage.py migrate || echo "Migrate failed, trying alternative method..."

echo "Running collectstatic..."
python manage.py collectstatic --no-input

echo "Setting up database (Method 2: Management command)..."
python manage.py setup_db || echo "Setup_db failed, trying alternative method..."

echo "Setting up database (Method 3: Direct script)..."
python migrate.py || echo "Direct script failed, will try to continue anyway..."

echo "Build complete! If database setup failed, check the logs."