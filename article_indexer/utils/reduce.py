from typing import Callable, TypeVar, Iterable, Optional
from functools import reduce

# functools.reduce not really in use so far

T = TypeVar("T")

hmm = """
def shortcircuit(
    reducer: Callable[[bool, T], bool],
    iterable: Iterable[T],
) -> bool:
    it = iter(iterable)
    acc = True
    try:
        while True:
            acc = reducer(acc, next(it))
            if acc is None:
                return None
    except StopIteration:
        return acc
"""


# the initial value does not
def shortcircuit(
    reducer: Callable[[bool, T], bool],
    iterable: Iterable[T],
) -> bool:
    acc = True
    for item in iterable:
        acc = reducer(acc, item)
        if not acc:  # Short-circuit on False
            return False
    return True
