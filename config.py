from __future__ import annotations

from decouple import config as env

FLASK_SECRET_KEY = env('FLASK_SECRET_KEY')
# Directory to en-route the flask application and config
FLASK_APP = env('FLASK_APP')

FLASK_RUN_PORT = env('FLASK_RUN_PORT')

# Flask API web framework working environment
FLASK_ENV = env('FLASK_ENV')
# The environment, can be: "local", "test", "producccion"
ENVIRONMENT = env('ENVIRONMENT')

CONTENT_TYPE = env('CONTENT_TYPE')
URL_HOST = env('URL_HOST')
HEADERS = {'Content-Type': 'application/json'}
ENDPOINT_REQUEST = env('ENDPOINT_REQUEST')


"""
FLASK_SECRET_KEY=f35wQ+q+B.uH*s%MPR-mKD$t
FLASK_APP=src/layers/http_api/application
FLASK_ENV=development
FLASK_RUN_PORT=9000
ENVIRONMENT="local"

CONTENT_TYPE = 'application/json'
URL_HOST = 'https://cat-fact.herokuapp.com'
HEADERS = {'Content-Type': CONTENT_TYPE}
ENDPOINT_REQUEST = '/facts/random?animal_type=cat&amount=2'
"""