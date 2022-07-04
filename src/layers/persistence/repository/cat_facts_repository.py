"""This file intention is to provide repository for CatFacts"""
from __future__ import annotations

from src.layers.domain.model.cat_facts import CatFacts
from src.layers.persistence.base_repository import AbstractRepository
from src.adapters.persistence.api_client import APIClient


class CatFactsRepository(AbstractRepository):
    """Implementation of the abstract class of repository with get method"""

    def __init__(self, api_client: APIClient, cat_facts: CatFacts):
        self.api_client = api_client
        self.cat_facts_model = cat_facts

    def get(self):
        """
        Set get method to connect to API Client and request as GET HTTP Method from it

        :return: API response object from client connection
        """

        return self.api_client.connect()