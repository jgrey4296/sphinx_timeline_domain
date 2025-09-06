#!/usr/bin/env python3
"""
TEST File updated

"""
# ruff: noqa: ANN201, ARG001, ANN001, ARG002, ANN202, B011

# Imports
from __future__ import annotations

# ##-- stdlib imports
import logging as logmod
import pathlib as pl
import warnings
# ##-- end stdlib imports

# ##-- 3rd party imports
import pytest
# ##-- end 3rd party imports

##--|
import pyparsing as pp
from .. import dsl
##--|

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
## isort: on
# ##-- end type checking

##-- logging
logging = logmod.getLogger(__name__)
##-- end logging

# Vars:

# Body:

class TestDSL:

    @pytest.fixture(scope="function")
    def setup(self):
        pass

    ##--|

    def test_sanity(self):
        assert(True is not False) # noqa: PLR0133

    def test_simple(self):
        match dsl.marker.parse_string(":tags"):
            case pp.ParseResults():
                assert(True)
            case x:
                assert(False), x


    @pytest.mark.parametrize("year", ["1922", "2", "25.CE", "25.BCE", "25,000.BCE"])
    def test_year(self, year):
        match dsl.any_year.parse_string(year):
            case pp.ParseResults() as res if "BCE" in year:
                assert(res.era == "BCE")
            case pp.ParseResults() as res if "CE" in year:
                assert(res.era == "CE")
            case pp.ParseResults():
                assert(True)
            case x:
                assert(False), x

    def test_event(self):
        match dsl.EVENT.parse_string('1925.BCE "An Event" :tags aweg,awef :tags bloo'):
            case pp.ParseResults() as res:
                assert("year" in res)
                assert("title" in res)
                assert("extras" in res)
            case x:
                assert(False), x


    def test_period(self):
        match dsl.PERIOD.parse_string('1925.CE -> 1930.CE "A period"'):
            case pp.ParseResults() as res:
                assert("start" in res)
                assert("end" in res)
                assert("title" in res)
                breakpoint()
                pass
            case x:
                assert(False), x


    def test_marker_assignment(self):
        match dsl.extras.parse_string(':tags blah :desc bloo blah'):
            case pp.ParseResults() as res:
                assert(True)
            case x:
                assert(False), x

    ##--|

    @pytest.mark.skip
    def test_todo(self):
        pass
