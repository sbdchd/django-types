from collections.abc import Callable, Mapping, Sequence
from typing import Any, TypeAlias

from django.http.request import QueryDict
from django.urls.resolvers import ResolverMatch

# The values are passed through `str()` (unless they are bytes), so anything is valid.
_QueryType: TypeAlias = (
    Mapping[str, object]
    | Mapping[bytes, object]
    | Mapping[str | bytes, object]
    | Mapping[str, Sequence[object]]
    | Mapping[bytes, Sequence[object]]
    | Mapping[str | bytes, Sequence[object]]
    | Sequence[tuple[str | bytes, object]]
    | Sequence[tuple[str | bytes, Sequence[object]]]
)

def resolve(path: str, urlconf: str | None = ...) -> ResolverMatch: ...
def reverse(
    viewname: Callable[..., Any] | str | None,
    urlconf: str | None = ...,
    args: Sequence[Any] | None = ...,
    kwargs: dict[str, Any] | None = ...,
    current_app: str | None = ...,
    *,
    query: QueryDict | _QueryType | None = ...,
    fragment: str | None = ...,
) -> str: ...

reverse_lazy: Any

def clear_url_caches() -> None: ...
def set_script_prefix(prefix: str) -> None: ...
def get_script_prefix() -> str: ...
def clear_script_prefix() -> None: ...
def set_urlconf(urlconf_name: type[Any] | str | None) -> None: ...
def get_urlconf(default: None = ...) -> type[Any] | str | None: ...
def is_valid_path(path: str, urlconf: str | None = ...) -> bool: ...
def translate_url(url: str, lang_code: str) -> str: ...
