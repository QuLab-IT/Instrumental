# -*- coding: utf-8 -*-
#
# Instrumental documentation build configuration file, created by
# sphinx-quickstart on Tue Oct 29 15:34:22 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import datetime
import pkg_resources
import IPython

# Code taken from https://github.com/snide/sphinx_rtd_theme
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Only import and specify the rtd theme if we're building locally
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"


# Allow docs to build even without required modules
class Mock(object):
    __all__ = []

    def __init__(self, *args, **kwargs):
        pass

    def __getitem__(self, key):
        return Mock()

    def __iter__(self):
        return iter(())

    def __call__(self, *args, **kwargs):
        return Mock()

    def __mul__(self, other):
        return self

    def __cmp__(self, other):
        return 0  # For Quantity.dimesionality equality assertions

    @classmethod
    def __getattr__(cls, name):
        # Don't use type magic b/c it messes some things up
        if name in ('__file__', '__path__'):
            return '/dev/null'
        if name in ('__mro_entries__',):
            raise AttributeError
        else:
            return Mock()

# Include ctypes due to Windows-specific imports. This forces us to also mock numpy.cytypeslib to
# avoid a RecursionError.
MOCK_MODULES = ['numpy.ctypeslib','scipy', 'scipy.special', 'scipy.interpolate',
                'scipy.optimize', 'matplotlib', 'matplotlib.pyplot', 'matplotlib.widgets',
                'matplotlib.transforms', 'matplotlib.cbook', 'ctypes', 'ctypes.wintypes', 'visa',
                'pyvisa', 'pyvisa.constants', 'cffi', 'nicelib', 'win32event']

import sphinx.builders.linkcheck  # Force import before ctypes is mocked

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

#sys.path.insert(0, os.path.abspath('..'))
sys.path[0:0] = ['.', '..']

# Enable output of __init__ methods
def skip(app, what, name, obj, skip, options):
    if name == "__init__":
        excludes = options.get('exclude-members', [])
        return '__init__' in excludes
    return skip

def setup(app):
    app.connect("autodoc-skip-member", skip)

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.imgmath', 'sphinx.ext.autosummary',
              'sphinx.ext.napoleon', 'IPython.sphinxext.ipython_console_highlighting']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# Load metadata from __about__.py
base_dir = os.path.join(os.path.dirname(__file__), os.pardir)
about = {}
with open(os.path.join(base_dir, 'src', 'instrumental', '__about__.py')) as f:
    exec(f.read(), about)

# General information about the project.
project = u'Instrumental'
copyright = u'2013-{}, Nate Bogdanowicz'.format(datetime.date.today().year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = about['__version__']
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = 'py:obj'
autodoc_member_order = 'groupwise'

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '../images/logo.svg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Instrumentaldoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Instrumental.tex', u'Instrumental Documentation',
   u'Mabuchi Lab', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'instrumental', u'Instrumental Documentation',
     [u'Mabuchi Lab'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Instrumental', u'Instrumental Documentation',
   u'Mabuchi Lab', 'Instrumental', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
