"""..."""
# mypy: ignore-errors
from __future__ import annotations

import json
from urllib.parse import urlencode
from flask import Blueprint
from flask import request
import config
from src.layers.domain.model.facts import Facts
from src.adapters.persistence.api_client import APIClient
from src.adapters.persistence.api_client import APIConfig
from src.layers.http_api.bridge.controller.cat_facts_request_handler import CatFactsRequestHandler
# from src.layers.http_api.bridge.utils import query_string_transform
from src.layers.persistence.uow.cat_facts_uow import CatFactsUOW
from src.layers.services.cat_facts_service import CatFactsService

cat_facts_request = Blueprint('cat-facts', __name__, url_prefix='/v1/cat-facts')


def _initialize(animal_type, fact_amount):

    cat_facts_model = Facts(animal_type, fact_amount)

    params = {"animal_type": cat_facts_model.animal_type,
              "amount": cat_facts_model.fact_amount}

    # animal_type=cat&amount=2
    params_endpoint_request = urlencode(params)
    # params_endpoint_request = query_string_transform._get_query_string(params)

    url_host = config.URL_HOST
    http_method = 'GET'
    headers = config.HEADERS
    endpoint_request = config.ENDPOINT_REQUEST + params_endpoint_request

    api_config = APIConfig(url_host, endpoint_request, http_method, headers)

    api_client = APIClient(api_config)

    # Initialize services and handlers
    cat_facts_services = CatFactsService(CatFactsUOW(url_host, endpoint_request, http_method, headers, api_client))
    cat_facts_request_handler = CatFactsRequestHandler(cat_facts_services, cat_facts_model)

    return cat_facts_request_handler


@cat_facts_request.get('/<facts>')
def get_a_company(facts):
    '''..'''

    animal_type = "cat"

    request_handler = _initialize(animal_type, facts)

    page = request.args.get('page')
    showing_range = request.args.get('showing_range')

    response = request_handler.get_cat_facts(facts, page, showing_range)

    return response
