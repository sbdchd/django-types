from collections.abc import Callable
from typing import Any, TypeVar, overload

_T = TypeVar("_T")

@overload
def deconstructible(klass: type[_T]) -> type[_T]: ...
@overload
def deconstructible(*args: Any, path: str | None = ...) -> Callable[[type[_T]], type[_T]]: ...
