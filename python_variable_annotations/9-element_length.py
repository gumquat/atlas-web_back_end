#!/usr/bin/env python3

"""Description text goes here"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    _summary_

    Args:
    lst (List[str]): _description_

    Returns:
    List[Tuple[str, int]]: _description_
    """
    return [(i, len(i)) for i in lst]
