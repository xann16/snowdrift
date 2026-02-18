# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# TODO - cleanup and re-enable ruff / mypy

# to enable doctests ?
import sys
import os
from pathlib import Path
import snowdrift

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.path.insert(0, os.path.abspath('../../src/snowdrift'))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'snowdrift'
copyright = '2026, Maciej Manna'
author = 'Maciej Manna'

version = '.'.join(snowdrift.__version__.split('.')[:3])
release = snowdrift.__version__

pygments_style = 'sphinx'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # https://www.sphinx-doc.org/en/master/tutorial/automatic-doc-generation.html
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',  # creates .nojekyll in the output to discover static assets
    'sphinx.ext.todo'
]

templates_path = ['_templates']
exclude_patterns = []

autosummary_generate = True

autodoc_default_options = {'show-inheritance': None}
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,  # Keep the navigation sidebar expanded
    'navigation_depth': 4,  # Set the depth of the navigation sidebar
    'display_version': True
}
html_static_path = ['_static']
