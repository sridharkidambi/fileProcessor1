from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
import namedtupled



class StepsEntity:
   
   def __init__(self,stepsEvaluator:any):
        self.stepsEvaluator=stepsEvaluator

   def getEntity(self):
        return self.stepsEvaluator