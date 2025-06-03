from pathlib import Path
import pytest
from article_indexer.validate.markdown import has_valid_frontmatter

TEST_CASES_VALID = [
    ("valid", "with_json_frontmatter.md", True),
    ("valid", "with_toml_frontmatter.md", True),
    ("valid", "with_yaml_frontmatter.md", True),
    # ("valid", "no_frontmatter.md", True), #  valid markdown with no frontmatter
    ("valid", "edge_empty_json_frontmatter.md", True),
    ("valid", "edge_empty_toml_frontmatter.md", True),
    ("valid", "edge_empty_yaml_frontmatter.md", True),
]

TEST_CASES_INVALID = [
    ("invalid", "json_frontmatter_1.md", False),
    ("invalid", "json_frontmatter_2.md", False),
    ("invalid", "json_frontmatter_3.md", False),
    ("invalid", "toml_frontmatter_1.md", False),
    ("invalid", "toml_frontmatter_2.md", False),
    ("invalid", "toml_frontmatter_3.md", False),
    ("invalid", "yaml_frontmatter_1.md", False),
    ("invalid", "yaml_frontmatter_2.md", False),
    ("invalid", "yaml_frontmatter_3.md", False),
]


@pytest.mark.parametrize(
    "subdir,filename,expected", [*TEST_CASES_VALID, *TEST_CASES_VALID]
)
def test_has_valid_frontmatter(subdir: str, filename: str, expected: bool):
    test_file_path = Path.cwd() / "tests" / "data" / "markdown" / subdir / filename

    with open(test_file_path, "r", encoding="utf-8") as f:
        content = f.read()
    result = has_valid_frontmatter(content)

    assert result == expected, (
        f"Failed on {filename}: " f"Expected {expected}, got {result}"
    )
