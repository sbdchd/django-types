from collections.abc import Callable
from typing import Any, TypeVar, overload

from django.utils.functional import _StrOrPromise

_C = TypeVar("_C", bound=Callable[..., Any])

@overload
def staff_member_required(
    view_func: _C,
    redirect_field_name: str | None = ...,
    login_url: _StrOrPromise = ...,
) -> _C: ...
@overload
def staff_member_required(
    view_func: None = ...,
    redirect_field_name: str | None = ...,
    login_url: _StrOrPromise = ...,
) -> Callable[..., Any]: ...
