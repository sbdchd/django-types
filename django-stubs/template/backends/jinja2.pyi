from collections.abc import Callable, Mapping
from typing import Any
from typing_extensions import override

from django.http.request import HttpRequest
from django.template import base
from django.template.exceptions import TemplateSyntaxError
from django.utils.safestring import SafeText

from .base import BaseEngine

class Jinja2(BaseEngine):
    context_processors: list[str] = ...
    @override
    def from_string(self, template_code: str) -> Template: ...
    @override
    def get_template(self, template_name: str) -> Template: ...
    @property
    def template_context_processors(self) -> list[Callable[..., Any]]: ...

class Template:
    template: base.Template
    backend: Jinja2
    origin: Origin
    def __init__(self, template: base.Template, backend: Jinja2) -> None: ...
    def render(
        self,
        context: Mapping[str, Any] | None = ...,
        request: HttpRequest | None = ...,
    ) -> SafeText: ...

class Origin:
    name: str = ...
    template_name: str | None = ...
    def __init__(self, name: str, template_name: str | None) -> None: ...

def get_exception_info(exception: TemplateSyntaxError) -> dict[str, Any]: ...
