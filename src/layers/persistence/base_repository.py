'''Intention: provide CRUD methods and be injected in the uow'''
from __future__ import annotations

import abc


class AbstractRepository(abc.ABC):
    """Abstract class with the purpose of provide CRUD methods
    and be injected in the uow"""

    @abc.abstractmethod
    def get(self):
        """
        Get domain model

        Returns: Response model
        """
        raise NotImplementedError
