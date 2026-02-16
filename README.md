# snowdrift
Python package for generating optimized settings handlers (especially for HPC use) in C++ and other languages.

[![Coverage Status](https://codecov.io/gh/xann16/snowdrift/branch/main/graph/badge.svg)](https://app.codecov.io/gh/xann16/snowdrift)

# Links

- [Documentation (Simple PyDoc dump ATM)](https://xann16.github.io/snowdrift/)

# Quick Dev Basics (WIP)

Initial dev setup:

```shell
uv sync --frozen
uv run pre-commit install --install-hooks
```

Running tests:

```shell
uv run pytest
```

or with code coverage report (exported to HTML):

```shell
uv run pytest --cov=src/snowdrift --cov-report html
```

Manually running `pre-commit` checks (including `ruff` linting / formatting and `mymp` type checking):

```shell
uv run pre-commit run -a --hook-stage manual
```

Running snowdrift CLI:

```shell
uv run snowdrift
```

### Testing `sybil`

```python
x = 2
assert x == 2
```
