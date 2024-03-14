#!/usr/bin/env python3
"""Contains the function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Passes its float argument to a callable function"""
    def multiplier_function(number: float) -> float:
        """Multiples a number by multiplier"""
        return number * multiplier

    return multiplier_function
