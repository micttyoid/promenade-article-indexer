import pytest
from article_indexer.utils.reduce import shortcircuit
from typing import Callable, Iterable, TypeVar

T = TypeVar("T")


@pytest.mark.parametrize(
    "reducer,iterable,expected",
    [
        # Case: All True
        (lambda acc, x: True, [1, 2, 3], True),
        (lambda acc, x: True, [], True),
        # Case: Terminate early(at 5 and -2)
        (lambda acc, x: x % 2 == 0, [2, 4, 5, 6], False),
        (lambda acc, x: x > 0, [1, -2, 3], False),
        # Case: Stop at first iteration
        (lambda acc, x: bool(x), [0, 1, 2], False),
    ],
)
def test_utils_reduce_shortcircuit_basic(
    reducer: Callable[[bool, T], bool], iterable: Iterable[T], expected: bool
):
    assert shortcircuit(reducer, iterable) == expected


def test_utils_reduce_shortcircuit_order():
    """Process according to the order of iterable"""
    processed = []

    def tracker(acc: bool, x: int) -> bool:
        processed.append(x)
        return x > 0

    result = shortcircuit(tracker, [1, 2, -3, 4])

    assert result is False
    assert processed == [1, 2, -3]  # Should not process 4


def test_utils_reduce_shortcircuit_consumption():
    """Leave out the rest of iterable at termination"""

    def gen():
        yield 1
        yield 2
        pytest.fail("Supposedly unreachable here")
        yield 3

    result = shortcircuit(lambda acc, x: False, gen())
    assert result is False


# Raises error at invalid argument


def test_utils_reduce_shortcircuit_invalid_arg_reducer():
    with pytest.raises(TypeError):
        shortcircuit("A string. which is not a function", [1, 2, 3])  # type: ignore


def test_utils_reduce_shortcircuit_invalid_arg_iterable():
    with pytest.raises(TypeError):
        shortcircuit(lambda a, b: True, 123)  # type: ignore
