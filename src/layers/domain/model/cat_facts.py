"""This file intention is to provide the class CatFacts and its business rules"""
from __future__ import annotations

from dataclasses import dataclass

from src.layers.domain.exceptions import InvalidFactsRange


@dataclass
class CatFacts:
    """CatGFacts model to looking for data from API Client requested"""

    facts: float

    def __validate_facts_range(self):

        is_valid_facts_range = False

        if 1 <= self.facts <= 500:
            is_valid_facts_range = True

        if not is_valid_facts_range:
            raise InvalidFactsRange('Fact cant be less than 501 and more than 0')
