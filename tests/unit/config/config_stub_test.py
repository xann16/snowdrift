"""Tests for snowdrift.config.stub."""

from snowdrift.config.stub import answer, hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello(5) == 'Hello from config! The answer is 5!'


def test_answer() -> None:
    """Test the answer function."""
    assert answer() == 42
