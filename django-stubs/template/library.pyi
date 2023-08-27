from collections.abc import Callable
from typing import Any

from django.template.base import FilterExpression, Origin, Parser, Token
from django.template.context import Context
from django.utils.safestring import SafeText

from .base import Node, Template

class InvalidTemplateLibrary(Exception): ...

class Library:
    filters: dict[str, Callable[..., Any]] = ...
    tags: dict[str, Callable[..., Any]] = ...
    def __init__(self) -> None: ...
    def tag(
        self,
        name: Callable[..., Any] | str | None = ...,
        compile_function: Callable[..., Any] | str | None = ...,
    ) -> Callable[..., Any]: ...
    def tag_function(self, func: Callable[..., Any]) -> Callable[..., Any]: ...
    def filter(
        self,
        name: Callable[..., Any] | str | None = ...,
        filter_func: Callable[..., Any] | str | None = ...,
        **flags: Any
    ) -> Callable[..., Any]: ...
    def filter_function(
        self, func: Callable[..., Any], **flags: Any
    ) -> Callable[..., Any]: ...
    def simple_tag(
        self,
        func: Callable[..., Any] | str | None = ...,
        takes_context: bool | None = ...,
        name: str | None = ...,
    ) -> Callable[..., Any]: ...
    def inclusion_tag(
        self,
        filename: Template | str,
        func: None = ...,
        takes_context: bool | None = ...,
        name: str | None = ...,
    ) -> Callable[..., Any]: ...

class TagHelperNode(Node):
    func: Any = ...
    takes_context: Any = ...
    args: Any = ...
    kwargs: Any = ...
    def __init__(
        self,
        func: Callable[..., Any],
        takes_context: bool | None,
        args: list[FilterExpression],
        kwargs: dict[str, FilterExpression],
    ) -> None: ...
    def get_resolved_arguments(
        self, context: Context
    ) -> tuple[list[int], dict[str, SafeText | int]]: ...

class SimpleNode(TagHelperNode):
    args: list[FilterExpression]
    func: Callable[..., Any]
    kwargs: dict[str, FilterExpression]
    origin: Origin
    takes_context: bool | None
    token: Token
    target_var: str | None = ...
    def __init__(
        self,
        func: Callable[..., Any],
        takes_context: bool | None,
        args: list[FilterExpression],
        kwargs: dict[str, FilterExpression],
        target_var: str | None,
    ) -> None: ...

class InclusionNode(TagHelperNode):
    args: list[FilterExpression]
    func: Callable[..., Any]
    kwargs: dict[str, FilterExpression]
    origin: Origin
    takes_context: bool | None
    token: Token
    filename: Template | str = ...
    def __init__(
        self,
        func: Callable[..., Any],
        takes_context: bool | None,
        args: list[FilterExpression],
        kwargs: dict[str, FilterExpression],
        filename: Template | str | None,
    ) -> None: ...

def parse_bits(
    parser: Parser,
    bits: list[str],
    params: list[str],
    varargs: str | None,
    varkw: str | None,
    defaults: tuple[bool | str] | None,
    kwonly: list[str],
    kwonly_defaults: dict[str, int] | None,
    takes_context: bool | None,
    name: str,
) -> tuple[list[FilterExpression], dict[str, FilterExpression]]: ...
def import_library(name: str) -> Library: ...
