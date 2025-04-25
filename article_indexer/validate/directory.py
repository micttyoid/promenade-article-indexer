from pathlib import Path
from typing import Callable, List

from article_indexer.config import config
from article_indexer.utils.debugs import print_debug
from article_indexer.validate.index import is_valid_index_file
from article_indexer.utils.errors import IndexFormatError


def dir_has_valid_index_file(
    index_files: List[str] = [".pidx"],
) -> Callable[[Path], bool]:
    """
    Terminate iteration if invalid format of correctly named index file found
    Terminate iteration if not at least one valid index file found
    Pass otherwise
    """

    def _dir_has_valid_index_file(path: Path) -> bool:
        is_any = False
        for file in index_files:
            # Valid naming
            if path.stem == file:
                # Validate format
                if is_valid_index_file(file):
                    is_any = True
                else:
                    # Terminate by shortcircuits
                    if not config.LENIENT:
                        return False
                    # continue iteration
                    is_any = True
        return is_any

    return _dir_has_valid_index_file
