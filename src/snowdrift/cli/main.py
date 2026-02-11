"""Docstring for snowdrift.cli."""

import sys

from snowdrift import __version__
from snowdrift.core.stub import answer, hello


def main() -> int:
    """Main function for the snowdrift CLI."""
    print(f'Snowdrift v{__version__} - Work in progress!')
    print(hello(answer()))
    return 0


if __file__ == '__main__':
    sys.exit(main())
