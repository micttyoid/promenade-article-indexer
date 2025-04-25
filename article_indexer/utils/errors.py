import warnings
from typing import Optional, TypeVar, Type, Any
from article_indexer.config import config

T = TypeVar("T")

TODO = """
test like following
@pytest.fixture
def LENIENT():
    original = config.LENIENT
    config.LENIENT = True
    yield
    config.LENIENT = original
"""


class LenientError(Exception):
    """Base class that automatically respects LENIENT from config"""

    # Class-level defaults (file-specific)
    _TEMPORARY_LENIENT: Optional[bool] = None
    SEVERITY_LEVELS = {"low": 0, "medium": 1, "high": 2}
    DEFAULT_SEVERITY: str = "medium"

    def __init__(
        self,
        message: str,
        *,
        severity: str = None,
        hint: Optional[str] = None,
        culprit: Optional[str] = None,
        **metadata: Any,
    ):
        self.message = message
        self.severity = self.SEVERITY_LEVELS.get(severity or self.DEFAULT_SEVERITY, 1)
        self.hint = hint
        self.culprit = culprit
        self.metadata = metadata
        super().__init__(self._format_message())

    @property
    def is_lenient(self) -> bool:
        """Resolves leniency with priority:
        1. File-specific setting (if set)
        2. Global config setting
        3. Default False
        """
        if self._TEMPORARY_LENIENT is not None:
            return self._TEMPORARY_LENIENT
        return config.LENIENT

    @classmethod
    def configure(cls, lenient: bool = None, default_severity: str = None) -> None:
        if lenient is not None:
            # only temporary
            cls._TEMPORARY_LENIENT = lenient
        if default_severity is not None:
            cls.DEFAULT_SEVERITY = default_severity

    def _format_message(self) -> str:
        parts = []
        if self.culprit:
            parts.append(f"[{self.culprit}]")
        parts.append(self.message)
        if self.hint:
            parts.append(f"\nHINT: {self.hint}")
        if self.metadata:
            parts.append(f"\nMETADATA: {self.metadata}")
        return " ".join(parts)

    def handle(self) -> None:
        """Handle error according to current configuration."""
        if self.is_lenient:
            warnings.warn(
                f"Lenient mode caught {self.__class__.__name__}: {str(self)}",
                RuntimeWarning,
                stacklevel=2,
            )
            return
        raise self

    @classmethod
    def execute(
        cls: Type["LenientError"], func, *args, fallback: T = None, **kwargs
    ) -> T:
        """Execute a function with lenient error handling."""
        try:
            return func(*args, **kwargs)
        except cls as e:
            e.handle()
            return fallback


class ValidationError(LenientError):
    """For data validation failures."""

    DEFAULT_SEVERITY = "medium"

    def __init__(self, field: str, value: Any, rule: str, **kwargs):
        message = f"Validation failed for field '{field}': {rule} (got {value!r})"
        super().__init__(message, **kwargs)


class ConfigError(LenientError):
    """For configuration-related issues."""

    DEFAULT_SEVERITY = "high"

    def __init__(self, config_key: str, **kwargs):
        message = f"Invalid configuration for key '{config_key}'"
        super().__init__(message, **kwargs)


class IndexFormatError(Exception):
    """Raised when invalid index file is found"""


# TODO: index format-related detailed errors


class IndexlessDirectoryError(Exception):
    """Raised when given directory does not have index file"""


# Common format-level errors(before within the indexer's spec)
# - ex. Yaml, Markdown, ...


class YamlFormatError(Exception):
    """Raised when invalid YAML file is found"""


class MarkdownFormatError(Exception):
    """Raised when invalid Markdown file is found"""
