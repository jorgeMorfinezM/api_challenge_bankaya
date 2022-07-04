"""Custom data structure that allow cat_facts_response"""
from __future__ import annotations

from src.layers.domain.exceptions import IsNotModelError
from src.layers.domain.model.utils.base_dictionary import BaseDictionary
from src.layers.domain.model.cat_facts_response import CatFactsResponse


class CatFactsResponseDictionary(BaseDictionary):
    """CatFactsResponseDictionary its a custom data structure that allow CatFactsResponse"""

    def __setitem__(self, key, item: CatFactsResponse):
        if not isinstance(item, CatFactsResponse):
            raise IsNotModelError('Value it is not Company model')
        self.__dict__[key] = item
