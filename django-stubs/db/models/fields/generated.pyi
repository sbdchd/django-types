from typing import Any, Literal, TypeVar, overload
from django.db.models import Combinable

from collections.abc import Iterable

from . import Field, _ErrorMessagesToOverride, _ValidatorCallable

__all__ = ["GeneratedField"]

_A = TypeVar("_A", bound=Any | None)

class GeneratedField(Field[_A | Combinable, _A]):
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        *,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: Literal[False] = False,
        db_index: bool = ...,
        default: None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[Any, str] | tuple[str, Iterable[tuple[Any, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        db_default: None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> GeneratedField[_A]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        *,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: Literal[True],
        db_index: bool = ...,
        default: None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[Any, str] | tuple[str, Iterable[tuple[Any, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        db_default: None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> GeneratedField[_A | None]: ...
