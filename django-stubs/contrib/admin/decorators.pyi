from collections.abc import Callable, Sequence
from typing import Any, TypeVar

from django.contrib.admin import ModelAdmin
from django.db.models import Combinable, QuerySet
from django.db.models.base import Model
from django.db.models.expressions import BaseExpression
from django.http import HttpRequest, HttpResponse

_M = TypeVar("_M", bound=Model)
_T = TypeVar("_T", bound=object)

def action(
    function: (
        Callable[[ModelAdmin[_M], HttpRequest, QuerySet[_M]], HttpResponse | None]
        | None
    ) = ...,
    *,
    permissions: Sequence[str] | None = ...,
    description: str | None = ...,
) -> Callable[[_T], _T]: ...
def display(
    function: Callable[[_M], Any] | None = ...,
    *,
    boolean: bool | None = ...,
    ordering: str | Combinable | BaseExpression | None = ...,
    description: str | None = ...,
    empty_value: str | None = ...,
) -> Callable[[_T], _T]: ...
def register(*models: type[Model], site: Any | None = ...) -> Callable[[_T], _T]: ...
