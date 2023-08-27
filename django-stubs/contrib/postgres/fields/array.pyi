from collections.abc import Callable, Iterable
from typing import Any, Generic, Optional, TypeVar, Union, overload
from typing_extensions import Literal

from django.db.models.expressions import Combinable
from django.db.models.fields import Field, _ErrorMessagesToOverride, _ValidatorCallable

from .mixins import CheckFieldDefaultMixin

_V = TypeVar("_V", bound=Optional[Any])

class ArrayField(
    CheckFieldDefaultMixin,
    Generic[_V],
    Field[Union[_V, Combinable], _V],
):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    size: Optional[int] = ...
    default_validators: Any = ...
    from_db_value: Any = ...
    base_field: Field[_V, _V] = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        base_field: Field[Any, _V],
        size: Optional[int] = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[list[_V], Callable[[], list[_V]]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[tuple[list[_V], str], tuple[str, Iterable[tuple[list[_V], str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> ArrayField[list[_V]]: ...
    @overload
    def __new__(
        cls,
        base_field: Field[Any, _V],
        size: Optional[int] = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Optional[Union[list[_V], Callable[[], list[_V]]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[tuple[list[_V], str], tuple[str, Iterable[tuple[list[_V], str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> ArrayField[Optional[list[_V]]]: ...
    @property
    def description(self) -> str: ...  # type: ignore [override]
    def get_transform(self, name: Any) -> Any: ...
