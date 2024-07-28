import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Demineur'
author = 'SMoraisDev'
version = None
with open("../../src/VERSION") as f:
    version = f.readlines()[0]
release = version

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

html_theme = 'alabaster'
html_static_path = ['_static']
