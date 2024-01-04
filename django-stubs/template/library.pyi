from collections.abc import Callable
from typing import Any, TypeVar, overload
from typing_extensions import ParamSpec

from django.template.base import FilterExpression, Origin, Parser, Token
from django.template.context import Context
from django.utils.safestring import SafeText

from .base import Node, Template

T = TypeVar("T")
P = ParamSpec("P")

class InvalidTemplateLibrary(Exception): ...

class Library:
    filters: dict[str, Callable[..., Any]] = ...
    tags: dict[str, Callable[..., Any]] = ...
    def __init__(self) -> None: ...

    # Both arguments None
    @overload
    def tag(
        self,
        name: None = ...,
        compile_function: None = ...,
    ) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
    # Only name as function
    @overload
    def tag(
        self,
        name: Callable[P, T],
        compile_function: None = ...,
    ) -> Callable[P, T]: ...
    # Only name as string
    @overload
    def tag(
        self,
        name: str,
        compile_function: None = ...,
    ) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
    # Both arguments specified
    @overload
    def tag(
        self,
        name: str,
        compile_function: Callable[P, T],
    ) -> Callable[P, T]: ...
    def tag_function(self, func: Callable[P, T]) -> Callable[P, T]: ...

    # Both arguments None
    @overload
    def filter(
        self,
        name: None = ...,
        filter_func: None = ...,
        **flags: Any,
    ) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
    # Only name as string
    @overload
    def filter(
        self,
        name: str = ...,
        filter_func: None = ...,
        **flags: Any,
    ) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
    # Only name as callable
    @overload
    def filter(
        self,
        name: Callable[P, T],
        filter_func: None = ...,
        **flags: Any,
    ) -> Callable[P, T]: ...
    # Both arguments
    @overload
    def filter(
        self,
        name: str,
        filter_func: Callable[P, T],
        **flags: Any,
    ) -> Callable[P, T]: ...
    def filter_function(self, func: Callable[P, T], **flags: Any) -> Callable[P, T]: ...

    # func is None
    @overload
    def simple_tag(
        self,
        func: None = ...,
        takes_context: bool | None = ...,
        name: str | None = ...,
    ) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
    # func is callable
    @overload
    def simple_tag(
        self,
        func: Callable[P, T],
        takes_context: bool | None = ...,
        name: str | None = ...,
    ) -> Callable[P, T]: ...
    def inclusion_tag(
        self,
        filename: Template | str,
        func: None = ...,
        takes_context: bool | None = ...,
        name: str | None = ...,
    ) -> Callable[[Callable[P, T]], Callable[P, T]]: ...

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
