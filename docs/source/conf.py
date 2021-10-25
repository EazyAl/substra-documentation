# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sphinx_rtd_theme


class SubSectionTitleOrder:
    """Sort example gallery by title of subsection.
    Assumes README.txt exists for all subsections and uses the subsection with
    dashes, '---', as the adornment.

    This class is adapted from sklearn
    """

    def __init__(self, src_dir):
        self.src_dir = src_dir
        self.regex = re.compile(r"^([\w ]+)\n-", re.MULTILINE)

    def __repr__(self):
        return "<%s>" % (self.__class__.__name__,)

    def __call__(self, directory):
        src_path = os.path.normpath(os.path.join(self.src_dir, directory))

        # Forces Release Highlights to the top
        if os.path.basename(src_path) == "release_highlights":
            return "0"

        readme = os.path.join(src_path, "README.txt")

        try:
            with open(readme, "r") as f:
                content = f.read()
        except FileNotFoundError:
            return directory

        title_match = self.regex.search(content)
        if title_match is not None:
            return title_match.group(1)
        return directory

# -- Project information -----------------------------------------------------

project = u"Substra"
copyright = u"2020, OWKIN"
author = u"Owkin"
# The full version, including alpha/beta/rc tags
version = '0.1.0'  # TODO: include _get_version() when ready
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "sphinx.ext.ifconfig",
    "sphinx_click",
    "recommonmark",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx_gallery.gen_gallery",
    "sphinx_fontawesome"
]
todo_include_todos=True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
}

# This must be the name of an image file (path relative to the configuration
# directory) that is the favicon of the docs. Modern browsers use this as
# the icon for tabs, windows and bookmarks. It should be a Windows-style
# icon file (.ico).
html_favicon = "favicon.ico"

# this is needed for some reason...
# see https://github.com/numpy/numpydoc/issues/69
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# generate autosummary even if no references
autosummary_generate = True

# The suffix of source filenames.
source_suffix = '.rst'

# Generate the plot for the gallery
# plot_gallery = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

sphinx_gallery_conf = {
    "doc_module": "substra",
    "reference_url": {"Substra": None},
    "examples_dirs": ["../../examples"],
    "gallery_dirs": ["auto_examples"],
    "subsection_order": SubSectionTitleOrder("../../examples"),
}