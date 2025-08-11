import enum
import sys
from collections.abc import Sequence
from typing import Any, TypeVar

if sys.version_info < (3, 12):
    from typing import TypeAlias

    ChoicesType: TypeAlias = ChoicesMeta

else:
    type ChoicesType = ChoicesMeta

_EnumMemberT = TypeVar("_EnumMemberT")

class ChoicesMeta(enum.EnumMeta):
    names: list[str] = ...
    labels: list[str] = ...
    def __contains__(self, item: Any) -> bool: ...
    @property
    def values(self: type[_EnumMemberT]) -> Sequence[_EnumMemberT]: ...
    @property
    def choices(self: type[_EnumMemberT]) -> Sequence[tuple[_EnumMemberT, str]]: ...

class Choices(enum.Enum, metaclass=ChoicesMeta):
    def __str__(self) -> Any: ...
    @property
    def label(self) -> str: ...
    @property
    def value(self) -> Any: ...

class IntegerChoices(int, Choices):
    @property
    def value(self) -> int: ...

class TextChoices(str, Choices):
    @property
    def value(self) -> str: ...
