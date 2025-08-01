#!/usr/bin/env python3
"""This module provides a function that returns a list of tuples containing
elements and their lengths.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """Returns list of tuples: (element, length of element)."""
    return [(i, len(i)) for i in lst]
