from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
from stepProcessor import stepProcessor

class fileReaderProcessor(stepProcessor):
    
    def set_next(self, handler: handler):
        pass
    
    def handle(self, request):
        pass