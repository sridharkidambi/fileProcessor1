from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class handler(ABC):

    @abstractmethod
    def set_next(self, handler: handler):
        pass
    
    @abstractmethod
    def handle(self, request):
        pass