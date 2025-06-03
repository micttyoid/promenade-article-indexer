from pathlib import Path
from typing import Set, Tuple, Dict, Any, Optional
import re


def has_valid_frontmatter(md_content: str) -> bool:
    # Empty frontmatter is a valid frontmatter
    patterns = [
        r"^---\n(.*?\n)?---\n",  # yaml
        r"^\+\+\+\n(.*?\n)?\+\+\+\n",  # toml
        r"^;;;\n(.*?\n)?;;;\n",  # json
    ]

    return any(re.match(pattern, md_content, re.DOTALL) for pattern in patterns)
