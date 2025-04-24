from pathlib import Path
from typing import Callable


# Assuming the path is of directory
def has_valid_index_file(index_files: list[str] = [".pidx"]) -> Callable[[Path], bool]:
    """
    true of any of "index_files" exists
    """
    return lambda path: any((path / file).exists() for file in index_files)
