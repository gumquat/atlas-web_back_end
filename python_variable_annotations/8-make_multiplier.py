#!/usr/bin/env python3
from typing import Callable, float

"""Description text goes here"""


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
