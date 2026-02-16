# snowdrift
Python package for generating optimized settings handlers (especially for HPC use) in C++ and other languages.

[![Coverage Status](https://codecov.io/gh/xann16/snowdrift/branch/main/graph/badge.svg)](https://app.codecov.io/gh/xann16/snowdrift)

# IMPORTANT - Project in Initial Development

This project is in initial stages of active development and has not yet achieved even minimal functionality. Please refrain from installing it at this point. If You are interested, however, please read short plan and rationale behind it below, and provide Your feedback, ideas, or feature requests by [submitting an issue](https://xann16.github.io/snowdrift/).

THe idea behind `snowdrift` is to provide a generator that could convert simple description into a fully functioning configuration that could work in two different contests: setup and execution. This is inspired by the use case of many research, scientific or any other high-throughput (for HPC applications) software that has distinct setup (and cleanup) phase that has minimal impact on the entire run time, as well as execution phase which is highly optimized and runs for the most of the time with preset conditions. Such generated configuration could be freely and easily manipulated during setup, loaded from different common formats (JSON, YAML, TOML, XML, INI) or easily shared with other processes (e.g. via MPI). After necessary setup, such configuration could be converted to a highly performant, cache-friendly, and immutable (for both performance and safety) version usable during execution phase. The initial set of supported languages include compiled-languages common in HPC contexts - C, C++, and Fortran, as well as Python and Julia. Later, extensions to other languages are possible. More specific ideas will be made available here during the initial development stage.


# Links

- [Documentation (Testing + Simple Full API Docstring-based Dump)](https://xann16.github.io/snowdrift/)

# Quick Dev Basics (WIP)

(TODO: Update)

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
