import functools
from collections.abc import Callable, Sequence
from http.cookies import SimpleCookie
from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.template.base import Template
from django.template.context import RequestContext
from django.test.client import Client

class ContentNotRenderedError(Exception): ...

class SimpleTemplateResponse(HttpResponse):
    content: Any = ...
    closed: bool
    cookies: SimpleCookie[Any]
    status_code: int
    rendering_attrs: Any = ...
    template_name: list[str] | Template | str = ...
    context_data: dict[str, Any] | None = ...
    using: str | None = ...
    def __init__(
        self,
        template: list[str] | Template | str,
        context: dict[str, Any] | None = ...,
        content_type: str | None = ...,
        status: int | None = ...,
        charset: str | None = ...,
        using: str | None = ...,
    ) -> None: ...
    def resolve_template(
        self, template: Sequence[str] | Template | str
    ) -> Template: ...
    def resolve_context(
        self, context: dict[str, Any] | None
    ) -> dict[str, Any] | None: ...
    @property
    def rendered_content(self) -> str: ...
    def add_post_render_callback(self, callback: Callable[..., Any]) -> None: ...
    def render(self) -> SimpleTemplateResponse: ...
    @property
    def is_rendered(self) -> bool: ...
    def __iter__(self) -> Any: ...

class TemplateResponse(SimpleTemplateResponse):
    client: Client
    closed: bool
    context: RequestContext
    context_data: dict[str, Any] | None
    cookies: SimpleCookie[Any]
    csrf_cookie_set: bool
    json: functools.partial[Any]
    redirect_chain: list[tuple[str, int]]
    request: dict[str, int | str]
    status_code: int
    template_name: list[str] | Template | str
    templates: list[Template]
    using: str | None
    wsgi_request: WSGIRequest
    rendering_attrs: Any = ...
    def __init__(
        self,
        request: HttpRequest,
        template: list[str] | Template | str,
        context: dict[str, Any] | None = ...,
        content_type: str | None = ...,
        status: int | None = ...,
        charset: None = ...,
        using: str | None = ...,
    ) -> None: ...
