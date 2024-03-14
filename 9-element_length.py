#!/usr/bin/env python3
"""Properly annotates the function below"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Receives a list of strings and returns a list of tuples
    containing each string in the list and its length
    """
    return [(i, len(i)) for i in lst]
