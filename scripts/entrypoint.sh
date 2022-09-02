#!/bin/sh

echo $PORT
echo \n
echo \n

gunicorn -b 0.0.0.0:$PORT src:create_app
