#!/usr/bin/env python3
from typing import List, Tuple
"""Description text goes here"""

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
  """
  _summary_

  Args:
      lst (List[str]): _description_

  Returns:
      List[Tuple[str, int]]: _description_
  """
  return [(i, len(i)) for i in lst]
