from typing import Any, Callable, TypeVar, overload

_SD = TypeVar("_SD", bound="SafeData")

class SafeData:
    def __html__(self: _SD) -> _SD: ...

class SafeText(str, SafeData):
    @overload
    def __add__(self, rhs: SafeText) -> SafeText: ...
    @overload
    def __add__(self, rhs: str) -> str: ...
    @overload
    def __iadd__(self, rhs: SafeText) -> SafeText: ...
    @overload
    def __iadd__(self, rhs: str) -> str: ...

SafeString = SafeText

_C = TypeVar("_C", bound=Callable[..., Any])
@overload
def mark_safe(s: _SD) -> _SD: ...  # type: ignore
@overload
def mark_safe(s: _C) -> _C: ...
@overload
def mark_safe(s: Any) -> SafeText: ...
