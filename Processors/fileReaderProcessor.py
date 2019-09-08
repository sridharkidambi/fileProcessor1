from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
from stepProcessor import stepProcessor
from stepsEntity import stepsEntity

class fileReaderProcessor(stepProcessor):
    
    def handle(self, request:stepsEntity,seqNum:int):
        print("I am  in the fileReaderProcessor")
        pass