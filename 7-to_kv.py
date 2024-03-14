#!/usr/bin/env python3
"""Contains the function to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Recieves a string and an int/float, and returns a tuple
    containing the two items
    """
    return (k, v * v)
