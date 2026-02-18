"""Tests for snowdrift.breeze_cpp.stub."""

from snowdrift.breeze_cpp.stub import answer, hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello(5) == 'Hello from breeze (C++)! The answer is 5!'


def test_answer() -> None:
    """Test the answer function."""
    assert answer() == 42
