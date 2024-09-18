"""Module providing OS routines for NT or Posix depending on what system we're on"""
import os
import sys

sys.path.insert(0, os.path.abspath('../../src'))

PROJECT = 'Demineur'
AUTHOR = 'SMoraisDev'
VERSION = None

with open("../../src/VERSION", encoding="utf-8") as f:
    VERSION = f.readlines()[0]
release = VERSION

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = []

LANGUAGE = 'fr'

HTML_THEME = 'alabaster'
html_static_path = ['_static']
