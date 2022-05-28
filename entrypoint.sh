#!/bin/sh

set -o errexit
set -o nounset

# Clear Python Caches
find . -name "*.pyc" -exec rm -f {} \;

# Migrate django database changes
python manage.py makemigrations
python manage.py migrate --noinput

# Serve Static files into container
python manage.py collectstatic --noinput

exec "$@"