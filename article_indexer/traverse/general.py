from pathlib import Path
from typing import Callable
from article_indexer.utils.reduce import shortcircuit


# Wrapper for iterdir on shortcuit
def process_directory(
    root: Path,
    fn_file: Callable[[Path], bool],
    fn_dir: Callable[[Path], bool] = lambda _: True,
) -> bool:
    """
    Processes directories recursively.
    """

    def reducer(status: bool, path: Path) -> bool:
        if not status:
            return False

        if path.is_file():
            return fn_file(path)
        elif path.is_dir():
            return fn_dir(path) and process_directory(path, fn_file, fn_dir)
        return True

    return shortcircuit(reducer, root.iterdir())


def if_path_then(predicate: Callable[[Path], bool]) -> Callable[[Path], bool]:
    """
    Returns a function that conditionally applies `fn1` or `fn2` based on `predicate`
    """
    return lambda fn1, fn2: lambda path: fn1(path) if predicate(path) else fn2(path)
