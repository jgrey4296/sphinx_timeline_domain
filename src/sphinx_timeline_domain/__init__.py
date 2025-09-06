#!/usr/bin/env python3
# Imports:
from __future__ import annotations

# ##-- stdlib imports
import pathlib as pl
from collections.abc import Iterator
from importlib import metadata
from typing import Any, Final, Iterable

# ##-- end stdlib imports

# ##-- 3rd party imports
from jgdv import Maybe
from sphinx.errors import ExtensionError

# ##-- end 3rd party imports

from . import _interface as API
from .timeline_domain import TimelineDomain
from .parser import TimelineParser

__version__ = metadata.version("sphinx_timeline_domain")

##--|

def setup(app):
    # app.connect("html-page-context", tl_page_context)
    app.add_domain(TimelineDomain)
    # Parse timeline files:
    app.add_source_suffix(".timeline", "timeline")
    app.add_source_parser(TimelineParser)

    ## Config values:
    # absolute or relative to templates_path
    app.add_config_value("timeline_domain_entries_to_context", False, "html", bool)
    app.add_config_value("timeline_domain_templates", API.TEMPLATES_DIR, pl.Path)
