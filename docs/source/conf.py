import datetime
import os

# -- Project information -----------------------------------------------------
project = os.environ.get("PACKAGE_NAME", "evolving_ideas")
author = "Santiago Rincón <rincorpes@gmail.com>"
release = os.environ.get("CI_VERSION", "0.1.0")
copyright = f"{datetime.datetime.now().year} Santiago Rincón"

# -- General configuration ---------------------------------------------------
extensions = [
    "autoapi.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# AutoAPI config
autoapi_dirs = ["../../evolving_ideas"]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "special-members",
    "show-module-summary",
    "imported-members",
]
suppress_warnings = [
    "autoapi.python_import_resolution",
    "autoapi.not_readable",
]

# -- HTML output -------------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
# html_logo = "../../resources/logo/trivox-logo.png"
# html_favicon = "../../resources/logo/favicon-32x32.png"

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

todo_include_todos = True
autosummary_generate = True

html_theme_options = {
    "dark_css_variables": {
        "color-brand-primary": "#00e0ff",  # cyan from triangle
        "color-brand-content": "#a259ff",  # purple from eye
        "color-background-primary": "#0f0f0f",  # dark black
        "color-background-hover": "#1a1a1a",
        "color-background-hover--transparent": "#1a1a1a",
        "color-highlight-on-target": "#332e66",  # accent for headings or links
        "color-foreground-primary": "#ffffff",  # base text
    },
    "light_css_variables": {
        "color-brand-primary": "#00bfe6",  # muted cyan for light mode
        "color-brand-content": "#7c4dff",  # keep slight purple tint
        "color-background-primary": "#ffffff",
        "color-background-hover": "#f2f2f2",
        "color-background-hover--transparent": "#f9f9f9",
        "color-highlight-on-target": "#d6c8ff",  # soft violet highlight
        "color-foreground-primary": "#0f0f0f",  # dark text
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/trivox-io/evolving-ideas",
            "html": "",
            "class": "fa-brands fa-github",
        },
        {
            "name": "Discord",
            "url": "https://discord.gg/ER9Sryjd",
            "html": "",
            "class": "fa-brands fa-discord",
        },
    ],
}
