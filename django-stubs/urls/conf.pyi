from collections.abc import Callable, Coroutine
from typing import Any, overload

from ..conf.urls import IncludedURLConf
from ..http.response import HttpResponseBase
from .resolvers import URLPattern, URLResolver

_ResponseType = (
    HttpResponseBase | Coroutine[Any, Any, HttpResponseBase] | Coroutine[Any, Any, None]
)

def include(
    arg: Any, namespace: str | None = ...
) -> tuple[list[URLResolver], str | None, str | None]: ...

# path()
@overload
def path(
    route: str,
    view: Callable[..., _ResponseType],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLPattern: ...
@overload
def path(
    route: str, view: IncludedURLConf, kwargs: dict[str, Any] = ..., name: str = ...
) -> URLResolver: ...
@overload
def path(
    route: str,
    view: list[URLResolver | str],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...
@overload
def path(
    route: str,
    view: tuple[list[URLResolver | URLPattern], str, str],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...

# re_path()
@overload
def re_path(
    route: str,
    view: Callable[..., _ResponseType],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLPattern: ...
@overload
def re_path(
    route: str, view: IncludedURLConf, kwargs: dict[str, Any] = ..., name: str = ...
) -> URLResolver: ...
@overload
def re_path(
    route: str,
    view: list[URLResolver | str],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...
