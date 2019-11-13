web: gunicorn vfrlight.wsgi --log-file - 
worker: celery -A vfrlight worker  -E -B --loglevel=INFO
