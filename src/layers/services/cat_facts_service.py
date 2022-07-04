'''Define functionality on service layer'''
from __future__ import annotations

from src.layers.domain.model.cat_facts import CatFacts
from src.layers.domain.model.cat_facts_response import CatFactsResponse
from src.layers.domain.model.cat_facts_response_dictionary import CatFactsResponseDictionary
from src.layers.persistence.utils.cat_facts_serializer_response import CatFactsResponseSerializer
from src.layers.persistence.uow.cat_facts_uow import CatFactsUOW
from src.layers.domain.exceptions import IsNotModelError
from src.layers.services.exceptions import BaseCustomException
from src.layers.services.exceptions import IndexOutOfRange
from src.layers.services.exceptions import InvalidDictionaryFormat


class CatFactsService:

    def __init__(self, cat_facts_uow: CatFactsUOW, cat_facts: CatFacts):
        self.cat_facts_uow = cat_facts_uow
        self.cat_facts = cat_facts

    def get_cat_facts(self):

        if self.cat_facts.facts is None:
            raise IndexOutOfRange('Fact parameter not is an integer number or is empty')

        response = self.cat_facts_uow.cat_facts_repository.get(self.cat_facts.facts)

        if len(response) <= 0:
            raise BaseCustomException('Response is Empty, verify the API CatFacts endpoint on other service')

        cat_facts_response = [CatFactsResponseSerializer(cat_fact).cat_facts_response for cat_fact in response]

        for fact in cat_facts_response:

            fact_dictionary = CatFactsResponseDictionary()

            fact_dictionary.__setitem__(1, fact)

            if type(fact_dictionary) != dict:
                raise InvalidDictionaryFormat('Response does not have correct format')

        return cat_facts_response
