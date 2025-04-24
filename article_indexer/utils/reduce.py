from typing import Callable, TypeVar, Iterable, Optional
from functools import reduce

T = TypeVar("T")
S = TypeVar("S")

"""
def shortcircuit_reduce(
    func: Callable[[S, T], Optional[S]], iterable: Iterable[T], initial: S
) -> Optional[S]:
    it = iter(iterable)
    acc = initial
    try:
        while True:
            acc = func(acc, next(it))
            if acc is None:
                return None
    except StopIteration:
        return acc
"""


def shortcircuit_reduce(
    func: Callable[[S, T], bool],
    iterable: Iterable[T],
    initial: S,
) -> bool:
    acc = initial
    for item in iterable:
        acc = func(acc, item)
        if not acc:  # Short-circuit on False
            return False
    return True
