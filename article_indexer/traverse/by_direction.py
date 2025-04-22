from pathlib import Path


# TODO use pattern or list instead of 'index_file'
def upward(begin_path: Path, index_file=".pidx", fn=lambda path, index_file: True):
    """
    Traverse upward to the parent directory

    Args:
        index_file: The promenade index file, desirably in directories
        fn: Tells whether to continue traversal

    Returns:
        Path object of the last directory(including root) or None
    """
    current_path = begin_path

    # Continue until we reach the root directory
    while current_path != current_path.root:
        if fn(current_path, index_file):
            parent_path = current_path.parent

            # current_path is root
            if current_path == parent_path:
                # fn over root
                if fn(current_path, index_file):
                    # print("Root reached")
                    return current_path
                else:
                    return None

            current_path = parent_path
        else:
            return current_path


# TODO
def downward():
    pass
