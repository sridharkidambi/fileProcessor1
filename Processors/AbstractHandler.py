from Processors.Handler import Handler
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
from Processors.StepsEntity import StepsEntity

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