#!/bin/bash
#this is very basic and just the bare bones we need for Django and Angular. To use we have three options: install, build, and clean. 
# Exit immediately if a command exits with a non-zero status
set -e

# Define variables
PROJECT_DIR="$(pwd)"
BUILD_DIR="${PROJECT_DIR}/build"
LOG_FILE="${BUILD_DIR}/build.log"

# Create necessary directories
mkdir -p "$BUILD_DIR"

# Function to install backend (Django) dependencies
install_backend_dependencies() {
    echo "Installing Django backend dependencies..." | tee -a "$LOG_FILE"
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt >> "$LOG_FILE" 2>&1
    else
        echo "No requirements.txt found." | tee -a "$LOG_FILE"
    fi
}

# Function to build the backend (Django)
build_backend() {
    echo "Building Django backend..." | tee -a "$LOG_FILE"
    # Run migrations and prepare Django backend
    python manage.py migrate >> "$LOG_FILE" 2>&1
    # Collect static files (if needed for production)
    python manage.py collectstatic --noinput >> "$LOG_FILE" 2>&1
    echo "Django backend build complete." | tee -a "$LOG_FILE"
}

# Function to install frontend (Angular) dependencies
install_frontend_dependencies() {
    echo "Installing Angular frontend dependencies..." | tee -a "$LOG_FILE"
    cd frontend_directory
    npm install >> "$LOG_FILE" 2>&1
    cd "$PROJECT_DIR"
}

# Function to build the frontend (Angular)
build_frontend() {
    echo "Building Angular frontend..." | tee -a "$LOG_FILE"
    cd frontend_directory
    ng build --prod >> "$LOG_FILE" 2>&1
    cd "$PROJECT_DIR"
    echo "Angular frontend build complete." | tee -a "$LOG_FILE"
}

# Function to clean build artifacts
clean() {
    echo "Cleaning up..." | tee -a "$LOG_FILE"
    rm -rf "$BUILD_DIR"
}

# Main script logic based on input
case "$1" in
    install)
        install_backend_dependencies
        install_frontend_dependencies
        ;;
    build)
        build_backend
        build_frontend
        ;;
    clean)
        clean
        ;;
    *)
        echo "Usage: $0 {install|build|clean}"
        exit 1
        ;;
esac

echo "Build completed successfully." | tee -a "$LOG_FILE"
exit 0
