from collections.abc import Callable
from typing import Any

docutils_is_available: bool

def get_view_name(view_func: Callable[..., Any]) -> str: ...
def trim_docstring(docstring: Any) -> Any: ...
def parse_docstring(docstring: Any) -> Any: ...
def parse_rst(
    text: Any, default_reference_context: Any, thing_being_parsed: Any | None = ...
) -> Any: ...

ROLES: Any

def create_reference_role(rolename: Any, urlbase: Any) -> Any: ...
def default_reference_role(
    name: Any,
    rawtext: Any,
    text: Any,
    lineno: Any,
    inliner: Any,
    options: Any | None = ...,
    content: Any | None = ...,
) -> Any: ...

named_group_matcher: Any
unnamed_group_matcher: Any

def replace_named_groups(pattern: str) -> str: ...
def replace_unnamed_groups(pattern: str) -> str: ...
