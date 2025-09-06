#!/usr/bin/env python3
"""
The DSL for timelines

Parses text into a list of entries

"""
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

import pyparsing as pp
from pyparsing import pyparsing_common as ppc
from .. import _interface as API

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

__all__ = ["TIMELINE"]

# Vars:
_EXTRAS_kws = ["tags", "wiki", "url", "desc"]
# Body:

##-- pyparse
# Group, Suppress, ParseResults, Forward

# OnlyOnce, , FollowedBy, NotAny, OneOrMore, ZeroOrMore,
# Optional, SkipTo, Combine, Dict

# And, Each, MatchFirst, Or, CharsNotIn, Empty, Keyword,
# CaselessKeyword, Literal, CaselessLiteral,
# NoMatch, QuotedString, Regex, White, Word

#PARSER.setParseAction(lambda toks: toks))
#PARSER.setResultsName('')
#PARSER.parseString('')

##-- end pyparse

##--| utils
s            = pp.Suppress
op           = pp.Optional
opLn         = s(op(pp.LineEnd()))
COMMENT      = pp.Char("#")
ARROW        = pp.Keyword("->")

simple_word  = pp.Word(pp.alphanums)
word_list    = pp.Word(pp.alphanums + ",")
url          = ppc.url
quoted       = pp.dbl_quoted_string

short_num    = pp.Word(pp.nums)[1,4]
long_num     = pp.Word(pp.nums + ",")[...]

ce_year      = (
    short_num
    + op(s(pp.Literal(".")) + pp.Literal("CE"))
    )
b_ce_year  = (
    long_num
    + s(pp.Literal(".")) + pp.Literal("BCE")
)
any_year    = (b_ce_year | ce_year)

@any_year.set_parse_action
def unpack_year(toks):
    res = pp.ParseResults(toks[:])
    match toks.as_list():
        case [x]:
            res['year'] = x
            return res
        case [x, y]:
            res['year'] = x
            res['era']  = y
            return res
        case x:
            raise TypeError(type(x))

##--|
loc         = (quoted | word_list | simple_word)("loc")
people      = op(quoted | word_list | simple_word)("people")
title       = quoted.copy()

marker      = s(pp.Char(":")) + pp.one_of(_EXTRAS_kws)

assignment  = (
    marker
    + (quoted | url | word_list | simple_word)
    )

@assignment.set_parse_action
def pack_assignment(toks):
    return (toks[0], toks[1])

##--|
extras      = pp.ZeroOrMore(assignment)

@extras.set_parse_action
def accum_markers(toks:pp.ParseResults) -> list:
    return toks.as_list()

##--|
EVENT       = (
    any_year
    + title("title")
    + op(loc)
    + op(people)
    + pp.Group(extras)("extras")
)

@EVENT.set_parse_action
def build_event(toks) -> API.TLEvent:
    pass

PERIOD     = (
    any_year("start")
    + ARROW
    + any_year("end")
    + title("title")
    + op(loc)
    + op(people)
    + extras("extras")
)

@PERIOD.set_parse_action
def build_period(toks) -> API.TLPeriod:
    pass

TIMELINE   = pp.OneOrMore(PERIOD | EVENT)


