"""..."""
from __future__ import annotations

from datetime import datetime

from flask_api import status

from src.layers.domain.model.facts import Facts
from src.layers.domain.model.cat_facts_response import CatFactsResponse
from src.layers.http_api.bridge.serializer.json.cat_fact_response_schema import CatFactResponseSchema
from src.layers.services.cat_facts_service import CatFactsService


class CatFactsRequestHandler:
    """..."""

    def __init__(self, cat_facts_service: CatFactsService, cat_facts_model: Facts) -> None:
        self.cat_facts_service = cat_facts_service
        self.cat_facts_request_schema = CatFactResponseSchema()
        self.cat_facts_models = cat_facts_model

    @staticmethod
    def pagination(list_of_cat_facts, sample_range):
        """..."""

        return [list_of_cat_facts[i:i + sample_range] for i in range(0, len(list_of_cat_facts), sample_range)]

    @staticmethod
    def pagination_response(list_of_cat_facts, page):
        """..."""

        if page <= 0:
            raise Exception('Page cant be zero or negative')

        pages = len(list_of_cat_facts)

        list_of_companies = list_of_cat_facts[int(page) - 1]

        return {'pages': pages, 'resource': list_of_companies}

    def get_cat_facts(self, facts_params, page, showing_range):
        """..."""

        try:

            list_of_cat_facts = self.cat_facts_service.get_cat_facts(facts_params)

            list_of_cat_facts = [self.cat_facts_request_schema.dump(cat_facts) for cat_facts in list_of_cat_facts]

            list_of_cat_facts = self.pagination(list_of_cat_facts, int(showing_range))

            paginated_response = self.pagination_response(list_of_cat_facts, int(page))

        # pylint: disable=broad-except
        except Exception as exc:
            return {'error': exc.args[0]}, status.HTTP_400_BAD_REQUEST

        return paginated_response, status.HTTP_200_OK
