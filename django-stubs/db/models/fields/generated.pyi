from collections.abc import Iterable
from typing import Any, Literal, Never, TypeVar, overload

from django.db.models import Combinable, Expression, ForeignObjectRel
from django.db.models.expressions import Col

from . import Field, _ErrorMessagesToOverride, _ValidatorCallable
from .mixins import CheckFieldDefaultMixin

_GT = TypeVar("_GT", bound=Any | None)

class GeneratedField(CheckFieldDefaultMixin, Field[Never, _GT]):
    generated: Literal[True]
    db_returning: Literal[True]
    expression: Combinable | Expression

    @overload
    def __new__(
        cls,
        *,
        expression: Combinable | Expression,
        output_field: Field[Any, _GT],
        db_persist: bool,
        #
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: Literal[False] = False,
        db_index: bool = ...,
        rel: ForeignObjectRel | None = ...,
        editable: Literal[False] = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[Any, str] | tuple[str, Iterable[tuple[Any, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        auto_created: bool = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
        db_comment: str | None = ...,
    ) -> GeneratedField[_GT]: ...
    @overload
    def __new__(
        cls,
        *,
        expression: Combinable | Expression,
        output_field: Field[Any, _GT],
        db_persist: bool,
        #
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: Literal[True],
        db_index: bool = ...,
        rel: ForeignObjectRel | None = ...,
        editable: Literal[False] = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[Any, str] | tuple[str, Iterable[tuple[Any, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        auto_created: bool = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
        db_comment: str | None = ...,
    ) -> GeneratedField[_GT | None]: ...
    @property
    def cached_col(self) -> Col: ...
    def generated_sql(self, connection: Any) -> tuple[str, list[Any]]: ...

__all__ = ["GeneratedField"]
