"""This file intention is to provide uow for CatFacts"""
from __future__ import annotations

from src.layers.domain.model.cat_facts import CatFacts
from src.adapters.persistence.api_client import APIClient
from src.layers.persistence.base_uow import AbstractUnitOfWork
from src.layers.persistence.repository.cat_facts_repository import CatFactsRepository


class CatFactsUOW(AbstractUnitOfWork):
    """Implementation of the abstract class of unit of work
       with implementation of magic methods"""

    def __init__(self, api_client: APIClient, cat_facts: CatFacts):
        self.api_client = api_client
        self.cat_facts_model = cat_facts
        self.cat_facts_repository = CatFactsRepository(self.api_client, self.cat_facts_model)

    def __enter__(self):
        # pylint: disable=attribute-defined-outside-init
        self.api_client.connect()
        return super().__enter__()
