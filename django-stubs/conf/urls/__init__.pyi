# Stubs for django.conf.urls (Python 3.5)
from collections.abc import Callable
from typing import Any, overload

from django.http.response import HttpResponse, HttpResponseBase
from django.urls import URLPattern, URLResolver

handler400: str | Callable[..., HttpResponse] = ...
handler403: str | Callable[..., HttpResponse] = ...
handler404: str | Callable[..., HttpResponse] = ...
handler500: str | Callable[..., HttpResponse] = ...

IncludedURLConf = tuple[list[URLResolver], str | None, str | None]

def include(arg: Any, namespace: str = ..., app_name: str = ...) -> IncludedURLConf: ...
@overload
def url(
    regex: str,
    view: Callable[..., HttpResponseBase],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLPattern: ...
@overload
def url(
    regex: str, view: IncludedURLConf, kwargs: dict[str, Any] = ..., name: str = ...
) -> URLResolver: ...
@overload
def url(
    regex: str,
    view: list[URLResolver | str],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...
