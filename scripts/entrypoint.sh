#!/bin/sh

gunicorn -b 0.0.0.0:$PORT "src:create_app()"
