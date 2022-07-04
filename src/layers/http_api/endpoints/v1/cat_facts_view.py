'''..'''
# mypy: ignore-errors
from __future__ import annotations

import json

from flask import Blueprint
from flask import request
import config
from src.layers.domain.model.cat_facts import CatFacts
from src.adapters.persistence.api_client import APIClient
from src.adapters.persistence.api_client import APIConfig
from src.layers.http_api.bridge.controller.cat_facts_request_handler import CatFactsRequestHandler
from src.layers.persistence.uow.cat_facts_uow import CatFactsUOW
from src.layers.services.cat_facts_service import CatFactsService

cat_facts_request = Blueprint('cat-facts', __name__, url_prefix='/v1/cat-facts')

url_host = config.URL_HOST
http_method = config.HTTP_METHOD
headers = config.HEADERS
endpoint_request = config.ENDPOINT_REQUEST

cat_facts_model = CatFacts()

api_config = APIConfig(url_host, endpoint_request, http_method, headers, cat_facts_model)

api_client = APIClient(api_config)

# Initialize services and handlers
company_services = CatFactsService(CatFactsUOW(api_client, cat_facts_model), cat_facts_model)
company_request_handler = CatFactsRequestHandler(company_services, cat_facts_model)


@cat_facts_request.get('/<facts>')
def get_a_company(facts):
    '''..'''

    page = request.args.get('page')
    showing_range = request.args.get('showing_range')

    response = company_request_handler.get_cat_facts(facts, page, showing_range)

    return response
