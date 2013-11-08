#!/bin/bash
set -e
LOGFILE=/home/test1.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
ADDRESS=127.0.0.1:8000
DJANGO_WSGI_MODULE=homepage.wsgi 
# user/group to run as
USER=root
GROUP=root
exec gunicorn $DJANGO_WSGI_MODULE:application -c gunicorn.conf.py -w $NUM_WORKERS --bind=$ADDRESS --user=$USER --group=$GROUP --log-level=debug 
