# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime
from typing import Any


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
sys.path.insert(0, ".")
sys.path.append(os.path.abspath("../.."))

from fiderpy import __version__  # noqa: E402


project = "fider-py"
copyright = datetime.today().strftime("%Y, Nick Kelly")
author = "Nick Kelly"
release = __version__
version = ".".join(__version__.split(".", 2)[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
    "sphinx.ext.autodoc",
]

templates_path = ["_templates"]
exclude_patterns: list[str] = []
add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {"collapse_navigation": True}


def setup(app: Any) -> None:
    app.add_css_file("theme_override.css")
