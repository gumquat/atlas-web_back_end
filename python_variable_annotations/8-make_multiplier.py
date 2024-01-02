#!/usr/bin/env python3

"""Description text goes here"""
from typing import Callable, float


def make_multiplier(multiplier: float) -> Callable[[float], float]:
     """
     _summary_

     Args:
          multiplier (float): _description_

     Returns:
          Callable[[float], float]: _description_
     """
     def multiply(num: float) -> float:
          return num * multiplier
     return multiply
