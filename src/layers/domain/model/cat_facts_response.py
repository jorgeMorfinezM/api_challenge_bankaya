"""This file intention is to provide the class CatFactsResponse and its business rules"""
from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass


@dataclass
class CatFactsResponse:

    _id: str
    __v: int
    text: str
    updatedAt: datetime.utcnow()
    deleted: bool
    source: str
    sentCount: int
