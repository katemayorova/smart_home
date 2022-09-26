echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
gunicorn smart_home.wsgi -b 0.0.0.0:8000