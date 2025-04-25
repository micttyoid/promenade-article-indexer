from pathlib import Path
from typing import Callable
from article_indexer.traverse.general import process_directory
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


# TODO: symlink?
def downward(
    begin_path: Path,
    fn_file: Callable[[Path], bool],
    fn_dir: Callable[[Path], bool],
):
    return process_directory(begin_path, fn_file, fn_dir)


maybe = """
def downward(
    begin_path: Path,
    fn_dir: Callable[[Path], bool],
    fn_file: Callable[[Path], bool],
):
    return if_path_then(
        lambda path: path.is_dir() # fmt: skip
    )(
        lambda path: _downward_fn_dir_loop(path, fn_dir, fn_file),  # fmt: skip
        lambda path: fn_file(path) # fmt: skip
    )(
        begin_path
    )


def downward(begin_path: Path, fn: Callable[[Path], bool]):

    Recursively traverse all child directories starting from begin_path,
    applying the given function to each directory.
 
    # TODO: not sure if fn should determine

    return lambda path: if_path_then(
        lambda path: path.is_dir() # fmt: skip
    )(
        _has_valid_index_file(path), # fmt: skip        
        lambda path: True # fmt: skip
    )

    # Recursively process all subdirectories
    if begin_path.is_dir():
        for child_path in begin_path.iterdir():
            print(child_path)
            downward(child_path, fn)
    else:
        return fn(begin_path)

        # if child.is_dir():
"""
