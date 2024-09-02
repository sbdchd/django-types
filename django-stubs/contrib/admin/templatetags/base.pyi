from collections.abc import Callable
from typing import Any

from django.template.base import Parser, Token
from django.template.context import Context
from django.template.library import InclusionNode
from django.utils.safestring import SafeText

class InclusionAdminNode(InclusionNode):
    args: list[Any]
    func: Callable[..., Any]
    kwargs: dict[Any, Any]
    takes_context: bool  # pyright: ignore[reportIncompatibleVariableOverride]
    template_name: str = ...
    def __init__(
        self,
        parser: Parser,
        token: Token,
        func: Callable[..., Any],
        template_name: str,
        takes_context: bool = ...,
    ) -> None: ...
    def render(self, context: Context) -> SafeText: ...
