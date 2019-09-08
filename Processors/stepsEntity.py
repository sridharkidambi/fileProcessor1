from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
from stepProcessor import stepProcessor
import namedtupled

class stepsEntity:
   stepsEvaluator:namedtupled
   def __init__(self,stepsEvaluator):
       self.stepsEvaluator=stepsEvaluator
    

