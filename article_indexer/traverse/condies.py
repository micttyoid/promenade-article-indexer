from pathlib import Path
from typing import Callable


def if_path_then(predicate: Callable[[Path], bool]) -> Callable[[Path], bool]:
    """
    Returns a function that conditionally applies `fn1` or `fn2` based on `predicate`
    """
    return lambda fn1, fn2: lambda path: fn1(path) if predicate(path) else fn2(path)
