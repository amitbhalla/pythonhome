#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Creating directories..."
mkdir -p static
mkdir -p staticfiles

echo "Running collectstatic..."
python manage.py collectstatic --no-input

echo "Setting up database and loading seed data..."
python manage.py setup_db

echo "Build complete!"