from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
import StepsEntity

class Handler(ABC):
    
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[StepsEntity]:
        pass

class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: StepsEntity) -> StepsEntity:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None
