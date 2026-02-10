"""Tests for snowdrift.code_writer.stub."""

from snowdrift.code_writer.stub import answer, hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello(5) == 'Hello from code writer! The answer is 5!'


def test_answer() -> None:
    """Test the answer function."""
    assert answer() == 42
