from collections.abc import Callable, Iterable
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Literal

from django.db.models import Field, Transform

from .mixins import CheckFieldDefaultMixin

_Choice = tuple[Any, Any]
_ChoiceNamedGroup = tuple[str, Iterable[_Choice]]
_FieldChoices = Iterable[_Choice | _ChoiceNamedGroup]
_ValidatorCallable = Callable[..., None]
_ErrorMessagesToOverride = dict[str, Any]

_T = TypeVar("_T", bound=dict[str, str | None] | None)

class HStoreField(Generic[_T], CheckFieldDefaultMixin, Field[Any, Any]):
    @overload
    def __init__(
        self: HStoreField[dict[str, str | None]],
        verbose_name: str | bytes | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: _FieldChoices | None = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: HStoreField[dict[str, str | None] | None],
        verbose_name: str | bytes | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: _FieldChoices | None = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> None: ...
    def get_transform(self, name: Any) -> Any: ...
    def __get__(self, instance: Any, owner: Any) -> _T: ...
    def __set__(self, instance: Any, value: _T) -> None: ...

class KeyTransform(Transform):
    def __init__(self, key_name: str, *args: Any, **kwargs: Any) -> None: ...

class KeyTransformFactory:
    def __init__(self, key_name: str) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> KeyTransform: ...

class KeysTransform(Transform): ...
class ValuesTransform(Transform): ...
