from pathlib import Path
from typing import Callable, List

from article_indexer.validate.index import is_valid_index_file


# Assume path is regular file
# Assume shortcuit
def has_valid_index_file(index_files: List[str] = [".pidx"]) -> Callable[[Path], bool]:
    def _has_valid_index_file(path: Path) -> bool:
        if any(path.stem == file for file in index_files):
            return True
        else:
            return True

    return _has_valid_index_file
