exec celery -A worker:app beat --loglevel=info &
exec celery -A worker:app worker --concurrency=1