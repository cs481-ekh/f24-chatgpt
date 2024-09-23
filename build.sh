#!/bin/bash
#THIS IS VERY BASIC AND WE ARE LEARNING TO USE Django and Angular. But this is the basic installs we will need. 
# Exit on any error
set -e

# Backend: Django setup

echo "Building Django backend..."

# Install Python dependencies
pip install -r requirements.txt

# Run migrations (assumes a local SQLite database or pre-configured DB)
python manage.py migrate

# Collect static files (optional, if applicable)
# python manage.py collectstatic --noinput

echo "Django backend build complete."

# Frontend: Angular setup

echo "Building Angular frontend..."

# Navigate to your Angular project directory
cd frontend_directory

# Install Node.js dependencies
npm install

# Build the Angular app
ng build --prod

echo "Angular frontend build complete."

# Return 0 to indicate success
exit 0
