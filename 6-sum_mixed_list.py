#!/usr/bin/env python3
"""Contains the function sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Receives a list of ints and floats and returns the sum as a float"""
    return sum(mxd_lst)
