#!/usr/bin/env python3

"""Description text goes here"""
from typing import Union, tuple, float, str


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
    _summary_

    Args:
    k (str): _description_
    v (Union[int, float]): _description_

    Returns:
    tuple: _description_
    """
    return (k, pow(v, 2))
