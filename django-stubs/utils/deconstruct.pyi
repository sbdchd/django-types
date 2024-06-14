from collections.abc import Callable
from typing import Any, TypeVar, overload

T = TypeVar("T")

@overload
def deconstructible(klass: type[T]) -> type[T]: ...
@overload
def deconstructible(
    *args: Any, path: str | None = ...
) -> Callable[[type[T]], type[T]]: ...
