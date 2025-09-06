#!/usr/bin/env python3
"""

"""
# ruff: noqa:
from __future__ import annotations
# Imports:

# ##-- stdlib imports
import datetime
import enum
import functools as ftz
import itertools as itz
import logging as logmod
import pathlib as pl
import re
import time
import collections
import contextlib
import hashlib
from copy import deepcopy
from uuid import UUID, uuid1
from weakref import ref
import atexit # for @atexit.register
import faulthandler
# ##-- end stdlib imports

from docutils.statemachine import StringList # type: ignore[import-untyped]
from sphinx.parsers import RSTParser as SphinxParser # type: ignore[import-untyped]
from sphinx.util.logging import getLogger as getSphinxLogger

from . import _interface as API
from .util import dsl

# ##-- types
# isort: off
# General
import abc
import collections.abc
import typing
import types
from typing import cast, assert_type, assert_never
from typing import Generic, NewType, Never
from typing import no_type_check, final, override, overload
# Protocols and Interfaces:
from typing import Protocol, runtime_checkable
# isort: on
# ##-- end types

# ##-- type checking
# isort: off
if typing.TYPE_CHECKING:
    from typing import Final, ClassVar, Any, Self
    from typing import Literal, LiteralString
    from typing import TypeGuard
    from collections.abc import Iterable, Iterator, Callable, Generator
    from collections.abc import Sequence, Mapping, MutableMapping, Hashable

    from jgdv import Maybe
    from docutils import nodes
## isort: on
# ##-- end type checking

##-- logging
logging = logmod.getLogger(__name__)
sphlog = getSphinxLogger(__name__)
##-- end logging

# Vars:
# Body:

class TimelineParser(SphinxParser):
    """
    A Sphinx Parser for timeline files
    """
    supported : tuple[str, ...] = ("tl", "timeline") # type: ignore[assignment]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._templates = {
            "lib"     : "timeline_domain/lib.rst.jinja",
            "header"  : "timeline_domain/header.rst.jinja",
            "entry"   : "timeline_domain/entry.rst.jinja",
            "footer"  : "timeline_domain/footer.rst.jinja",
        }

    @override
    def set_application(self, app) -> None:
        super().set_application(app)

    @override
    def parse(self, inputstring:str|StringList, document:nodes.document) -> None:
        """ Parse a timeline file, generate equivalent rst, and parse that.

        """
        doc_source  = pl.Path(document['source'])
        rst = self.timeline_to_rst(inputstring)
        super().parse(rst, document)

    def timeline_to_rst(self, inputstring:str|StringList) -> str:
        result : str = ""
        match dsl.TIMELINE.parse_string(str(inputstring)):
            case []:
                pass

            case x:
                raise TypeError(type(x))

        return result
