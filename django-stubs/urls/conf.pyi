from collections.abc import Callable, Coroutine
from typing import Any, TypeAlias, overload

from django.utils.functional import _StrOrPromise

from ..conf.urls import IncludedURLConf
from ..http.response import HttpResponseBase
from .resolvers import URLPattern, URLResolver

_ResponseType: TypeAlias = HttpResponseBase | Coroutine[Any, Any, HttpResponseBase] | Coroutine[Any, Any, None]

def include(arg: Any, namespace: str | None = ...) -> tuple[list[URLResolver], str | None, str | None]: ...

# path()
@overload
def path(
    route: _StrOrPromise,
    view: Callable[..., _ResponseType],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLPattern: ...
@overload
def path(route: _StrOrPromise, view: IncludedURLConf, kwargs: dict[str, Any] = ..., name: str = ...) -> URLResolver: ...
@overload
def path(
    route: _StrOrPromise,
    view: list[URLResolver | str],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...
@overload
def path(
    route: _StrOrPromise,
    view: tuple[list[URLResolver | URLPattern], str, str],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...

# re_path()
@overload
def re_path(
    route: _StrOrPromise,
    view: Callable[..., _ResponseType],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLPattern: ...
@overload
def re_path(
    route: _StrOrPromise, view: IncludedURLConf, kwargs: dict[str, Any] = ..., name: str = ...
) -> URLResolver: ...
@overload
def re_path(
    route: _StrOrPromise,
    view: list[URLResolver | str],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...
