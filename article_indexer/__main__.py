"""
article_indexer.__main__

Main entry point for `python -m article_indexer`.
"""

import sys
import article_indexer.cmdline

try:
    sys.exit(article_indexer.cmdline.main_cli(sys.argv))
except KeyboardInterrupt:
    sys.exit(1)
