
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
from handler import handler

class stepProcessor(handler):
    

    _next_handler: handler = None

    def set_next(self, handler: handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None