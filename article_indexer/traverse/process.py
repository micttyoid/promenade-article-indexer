from typing import Callable
from pathlib import Path

from article_indexer.utils.reduce import shortcircuit_reduce


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

    return shortcircuit_reduce(reducer, root.iterdir(), True)
