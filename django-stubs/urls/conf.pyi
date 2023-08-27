from collections.abc import Callable, Coroutine
from typing import Any, Optional, Union, overload

from ..conf.urls import IncludedURLConf
from ..http.response import HttpResponseBase
from .resolvers import URLPattern, URLResolver

_ResponseType = Union[
    HttpResponseBase, Coroutine[Any, Any, HttpResponseBase], Coroutine[Any, Any, None]
]

def include(
    arg: Any, namespace: Optional[str] = ...
) -> tuple[list[URLResolver], Optional[str], Optional[str]]: ...

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
    view: list[Union[URLResolver, str]],
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
    view: list[Union[URLResolver, str]],
    kwargs: dict[str, Any] = ...,
    name: str = ...,
) -> URLResolver: ...
