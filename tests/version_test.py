"""TODO: Docstring for tests.version_test."""

from snowdrift import __version__


def test_version() -> None:
    """Test that the version is correctly set."""
    assert __version__ != ''
