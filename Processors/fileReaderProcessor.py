from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
from stepProcessor import stepProcessor

class fileReaderProcessor(stepProcessor):
    
    def handle(self, request,seqNum:int):
        print("I am  in the fileReaderProcessor")
        pass