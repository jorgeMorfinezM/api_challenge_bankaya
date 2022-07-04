from __future__ import annotations

from decouple import config as env

FLASK_SECRET_KEY = env('FLASK_SECRET_KEY')
# Directory to en-route the flask application and config
FLASK_APP = env('FLASK_APP')
# Flask API web framework working environment
FLASK_ENV = env('FLASK_ENV')
# The environment, can be: "local", "test", "producccion"
ENVIRONMENT = env('ENVIRONMENT')

CONTENT_TYPE = env('CONTENT_TYPE')

URL_HOST = env('ENVIRONMENT')
HTTP_METHOD = env('HTTP_METHOD')
HEADERS = {'Content-Type': 'application/json'}
ENDPOINT_REQUEST = env('ENDPOINT_REQUEST')
