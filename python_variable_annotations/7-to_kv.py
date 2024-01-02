#!/usr/bin/env python3
from typing import Union, tuple, float, str

def to_kv(k: str, v: Union[int, float]) -> tuple:
  return (k, pow(v, 2))
