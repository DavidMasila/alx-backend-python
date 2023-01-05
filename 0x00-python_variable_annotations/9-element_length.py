#!/usr/bin/env python3
"""
duck type an iterable object
"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
    Comments here
    """

    return [(i, len(i)) for i in lst]
