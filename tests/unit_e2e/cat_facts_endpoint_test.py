from __future__ import annotations

import json
import config
from urllib.parse import urlencode
from src.layers.domain.model.facts import Facts
from src.layers.domain.model.cat_facts_response import CatFactsResponse
from src.layers.persistence.utils.cat_facts_serializer_response import CatFactsResponseSerializer
from src.layers.http_api.application import app
from src.adapters.persistence.api_client import APIClient
from src.adapters.persistence.api_client import APIConfig
from src.layers.http_api.bridge.controller.cat_facts_request_handler import CatFactsRequestHandler
from src.layers.http_api.endpoints.v1 import cat_facts_view
from src.layers.persistence.uow.cat_facts_uow import CatFactsUOW
from src.layers.services.cat_facts_service import CatFactsService


def init_services(animal_type, fact_amount):
    cat_facts_model = Facts(animal_type, fact_amount)

    params = {"animal_type": cat_facts_model.animal_type,
              "amount": cat_facts_model.fact_amount}

    params_endpoint_request = urlencode(params)

    url_host = config.URL_HOST
    http_method = 'GET'
    headers = config.HEADERS
    endpoint_request = config.ENDPOINT_REQUEST + params_endpoint_request

    api_config = APIConfig(url_host, endpoint_request, http_method, headers)

    api_client = APIClient(api_config)

    cat_facts_service = CatFactsService(CatFactsUOW(url_host,
                                                    endpoint_request,
                                                    http_method,
                                                    headers,
                                                    api_client))
    cat_facts_request_handler = CatFactsRequestHandler(cat_facts_service, cat_facts_model)


def test_get_cat_facts():
    animal_type = "cat"
    fact_amount = 499

    init_services(animal_type, fact_amount)

    response = app.test_client().get('/v1/cat-facts/' + str(fact_amount))

    cat_facts_response = json.loads(response.data.decode('utf-8'))

    for cat_facts in cat_facts_response:
        cat_facts_serializer = CatFactsResponseSerializer(cat_facts)
        cat_fact_response = cat_facts_serializer.cat_facts_response

        assert isinstance(cat_facts, CatFactsResponse)
        assert cat_fact_response._id == cat_facts._id
        assert cat_fact_response.__v == cat_facts.__v
        assert cat_fact_response.text == cat_facts.text
        assert cat_fact_response.updatedAt == cat_facts.updatedAt
        assert cat_fact_response.deleted == cat_facts.deleted
        assert cat_fact_response.source == cat_facts.source
        assert cat_fact_response.sentCount == cat_facts.sentCount

    assert response.status_code == 200

