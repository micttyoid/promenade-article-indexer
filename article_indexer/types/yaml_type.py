from typing import TypeAlias, Dict, Any, Union

YamlType: TypeAlias = Union[
    Dict[str, Any],
    list,
    str,
    int,
    float,
    bool,
    None,
]
