#!/usr/bin/env python3
from typing import Callable, float

def make_multiplier(multiplier: float) -> Callable[[float], float]:
  def multiply(num: float) -> float:
       return num * multiplier
  return multiply
