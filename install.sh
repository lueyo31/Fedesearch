#!/bin/bash

# Get the current device's IP address
DEFAULT_IP=$(hostname -I | awk '{print $1}')

# Prompt user for environment variables
read -p "Enter FRONTEND_URL port (default: 52580): " FRONTEND_PORT
FRONTEND_PORT=${FRONTEND_PORT:-52580}
FRONTEND_URL="http://${DEFAULT_IP}:${FRONTEND_PORT}"

read -p "Enter BACKEND_URL port (default: 52582): " BACKEND_PORT
BACKEND_PORT=${BACKEND_PORT:-52582}
BACKEND_URL="http://${DEFAULT_IP}:${BACKEND_PORT}"

read -p "Enter SEARCH_API_URL port (default: 52584): " SEARXNG_PORT
SEARXNG_PORT=${SEARXNG_PORT:-52584}
SEARCH_API_URL="http://${DEFAULT_IP}:${SEARXNG_PORT}"

SEARXNG_HOSTNAME=${DEFAULT_IP}

# Export variables for Docker Compose
export FRONTEND_URL BACKEND_URL SEARCH_API_URL SEARXNG_PORT SEARXNG_HOSTNAME

# Build Docker images
docker build -t proyecto-final-back ./back || { echo "Failed to build backend image"; exit 1; }
docker build -t proyecto-final-front ./front/project || { echo "Failed to build frontend image"; exit 1; }

# Start containers using Docker Compose
docker-compose -f docker-compose.yml up --build