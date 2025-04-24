from pathlib import Path
from article_indexer.types.yaml_type import YamlType
import yaml


def load_yaml(yaml_path: Path) -> YamlType:
    """
    Load YAML file (duh)
    """
    try:
        with open(yaml_path, "r") as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as e:
                # Get the problem location if available
                if hasattr(e, "problem_mark"):
                    mark = e.problem_mark
                    error_msg = (
                        f"Invalid YAML syntax at line {mark.line+1}, column {mark.column+1}\n"
                        f"Error: {str(e)}"
                    )
                else:
                    error_msg = f"Invalid YAML: {str(e)}"
                raise ValueError(error_msg) from None
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file not found: {yaml_path}") from None


def is_valid_index_file(path: Path) -> bool:
    print("foo")
    yaml = load_yaml(path)
    print(yaml)
    return True
