from collections.abc import Callable, Mapping, Sequence
from typing import Any, Protocol, TypeVar, overload
from typing_extensions import Literal

from django.db.models import Manager, QuerySet
from django.db.models.base import Model
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.http.response import (
    HttpResponsePermanentRedirect as HttpResponsePermanentRedirect,
)
from django.http.response import HttpResponseRedirect as HttpResponseRedirect

def render_to_response(
    template_name: str | Sequence[str],
    context: Mapping[str, Any] | None = ...,
    content_type: str | None = ...,
    status: int | None = ...,
    using: str | None = ...,
) -> HttpResponse: ...
def render(
    request: HttpRequest,
    template_name: str | Sequence[str],
    context: Mapping[str, Any] | None = ...,
    content_type: str | None = ...,
    status: int | None = ...,
    using: str | None = ...,
) -> HttpResponse: ...

class SupportsGetAbsoluteUrl(Protocol): ...

@overload
def redirect(
    to: Callable[..., Any] | str | SupportsGetAbsoluteUrl,
    *args: Any,
    permanent: Literal[True],
    **kwargs: Any
) -> HttpResponsePermanentRedirect: ...
@overload
def redirect(
    to: Callable[..., Any] | str | SupportsGetAbsoluteUrl,
    *args: Any,
    permanent: Literal[False],
    **kwargs: Any
) -> HttpResponseRedirect: ...
@overload
def redirect(
    to: Callable[..., Any] | str | SupportsGetAbsoluteUrl,
    *args: Any,
    permanent: bool = ...,
    **kwargs: Any
) -> HttpResponseRedirect | HttpResponsePermanentRedirect: ...

_T = TypeVar("_T", bound=Model)

def get_object_or_404(
    klass: type[_T] | Manager[_T] | QuerySet[_T], *args: Any, **kwargs: Any
) -> _T: ...
def get_list_or_404(
    klass: type[_T] | Manager[_T] | QuerySet[_T], *args: Any, **kwargs: Any
) -> list[_T]: ...
def resolve_url(
    to: Callable[..., Any] | Model | str, *args: Any, **kwargs: Any
) -> str: ...
