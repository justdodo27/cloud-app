#!/bin/bash

# Wait for the PostgreSQL container to be ready
echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Run data loading script here if needed
python /app/load_data.py

exec "$@"
