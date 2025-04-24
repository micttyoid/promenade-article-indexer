from pathlib import Path
from typing import Callable
from warnings import warn


# TODO use pattern or list instead of 'index_files'
def upward(begin_path: Path, fn: Callable[[Path], bool]):
    """
    Traverse upward to the parent directory
    """
    current_path = begin_path

    # Continue until we reach the root directory
    while current_path != current_path.root:
        if fn(current_path):
            parent_path = current_path.parent
            # current_path is root
            if current_path == parent_path:
                # fn over root
                if fn(current_path):
                    warn("Reached root")
                    return current_path
                else:
                    return None

            current_path = parent_path
        else:
            return current_path


def downward(begin_path: Path, fn: Callable[[Path], bool]):
    """
    Recursively traverse all child directories starting from begin_path,
    applying the given function to each directory.
    """

    # TODO: not sure if fn should determine
    if not fn(begin_path):
        return

    # Recursively process all subdirectories
    for child in begin_path.iterdir():
        if child.is_dir():
            downward(child, fn)
