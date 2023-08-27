from collections.abc import Callable, Iterable
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Literal

from django.db.models.expressions import Combinable
from django.db.models.fields import Field, _ErrorMessagesToOverride, _ValidatorCallable

from .mixins import CheckFieldDefaultMixin

_V = TypeVar("_V", bound=Any | None)

class ArrayField(CheckFieldDefaultMixin, Generic[_V], Field[_V | Combinable, _V]):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    size: int | None = ...
    default_validators: Any = ...
    from_db_value: Any = ...
    base_field: Field[_V, _V] = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        base_field: Field[Any, _V],
        size: int | None = ...,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: list[_V] | Callable[[], list[_V]] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[list[_V], str] | tuple[str, Iterable[tuple[list[_V], str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> ArrayField[list[_V]]: ...
    @overload
    def __new__(
        cls,
        base_field: Field[Any, _V],
        size: int | None = ...,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: list[_V] | Callable[[], list[_V]] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[list[_V], str] | tuple[str, Iterable[tuple[list[_V], str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> ArrayField[list[_V] | None]: ...
    @property
    def description(self) -> str: ...  # type: ignore [override]
    def get_transform(self, name: Any) -> Any: ...
