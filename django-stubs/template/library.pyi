from collections.abc import Callable
from typing import Any, Optional, Union

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
        name: Optional[Union[Callable[..., Any], str]] = ...,
        compile_function: Optional[Union[Callable[..., Any], str]] = ...,
    ) -> Callable[..., Any]: ...
    def tag_function(self, func: Callable[..., Any]) -> Callable[..., Any]: ...
    def filter(
        self,
        name: Optional[Union[Callable[..., Any], str]] = ...,
        filter_func: Optional[Union[Callable[..., Any], str]] = ...,
        **flags: Any
    ) -> Callable[..., Any]: ...
    def filter_function(
        self, func: Callable[..., Any], **flags: Any
    ) -> Callable[..., Any]: ...
    def simple_tag(
        self,
        func: Optional[Union[Callable[..., Any], str]] = ...,
        takes_context: Optional[bool] = ...,
        name: Optional[str] = ...,
    ) -> Callable[..., Any]: ...
    def inclusion_tag(
        self,
        filename: Union[Template, str],
        func: None = ...,
        takes_context: Optional[bool] = ...,
        name: Optional[str] = ...,
    ) -> Callable[..., Any]: ...

class TagHelperNode(Node):
    func: Any = ...
    takes_context: Any = ...
    args: Any = ...
    kwargs: Any = ...
    def __init__(
        self,
        func: Callable[..., Any],
        takes_context: Optional[bool],
        args: list[FilterExpression],
        kwargs: dict[str, FilterExpression],
    ) -> None: ...
    def get_resolved_arguments(
        self, context: Context
    ) -> tuple[list[int], dict[str, Union[SafeText, int]]]: ...

class SimpleNode(TagHelperNode):
    args: list[FilterExpression]
    func: Callable[..., Any]
    kwargs: dict[str, FilterExpression]
    origin: Origin
    takes_context: Optional[bool]
    token: Token
    target_var: Optional[str] = ...
    def __init__(
        self,
        func: Callable[..., Any],
        takes_context: Optional[bool],
        args: list[FilterExpression],
        kwargs: dict[str, FilterExpression],
        target_var: Optional[str],
    ) -> None: ...

class InclusionNode(TagHelperNode):
    args: list[FilterExpression]
    func: Callable[..., Any]
    kwargs: dict[str, FilterExpression]
    origin: Origin
    takes_context: Optional[bool]
    token: Token
    filename: Union[Template, str] = ...
    def __init__(
        self,
        func: Callable[..., Any],
        takes_context: Optional[bool],
        args: list[FilterExpression],
        kwargs: dict[str, FilterExpression],
        filename: Optional[Union[Template, str]],
    ) -> None: ...

def parse_bits(
    parser: Parser,
    bits: list[str],
    params: list[str],
    varargs: Optional[str],
    varkw: Optional[str],
    defaults: Optional[tuple[Union[bool, str]]],
    kwonly: list[str],
    kwonly_defaults: Optional[dict[str, int]],
    takes_context: Optional[bool],
    name: str,
) -> tuple[list[FilterExpression], dict[str, FilterExpression]]: ...
def import_library(name: str) -> Library: ...
