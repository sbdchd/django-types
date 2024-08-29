from collections.abc import Callable, Iterable
from typing import Any, TypeVar, overload
from typing_extensions import Literal

from django.db.models.fields import CharField, EmailField, TextField

_Choice = tuple[Any, Any]
_ChoiceNamedGroup = tuple[str, Iterable[_Choice]]
_FieldChoices = Iterable[_Choice | _ChoiceNamedGroup]

_ValidatorCallable = Callable[..., None]
_ErrorMessagesToOverride = dict[str, Any]

_C = TypeVar("_C", bound=str | None)

class CIText: ...

class CICharField(CIText, CharField[_C]):
    @overload
    def __init__(
        self: CICharField[str],
        verbose_name: str | bytes | None = ...,
        *,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = False,
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
        self: CICharField[str | None],
        verbose_name: str | bytes | None = ...,
        *,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True],
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
    def __get__(self, instance: Any, owner: Any) -> _C: ...
    def __set__(self, instance: Any, value: _C) -> None: ...  # type: ignore [override]

class CIEmailField(CIText, EmailField[_C]):
    @overload
    def __init__(
        self: CIEmailField[str],
        verbose_name: str | bytes | None = ...,
        *,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = False,
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
        self: CIEmailField[str | None],
        verbose_name: str | bytes | None = ...,
        *,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True],
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
    def __get__(self, instance: Any, owner: Any) -> _C: ...
    def __set__(self, instance: Any, value: _C) -> None: ...  # type: ignore [override]

class CITextField(CIText, TextField[_C]):
    @overload
    def __init__(
        self: CITextField[str],
        verbose_name: str | bytes | None = ...,
        *,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = False,
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
        self: CITextField[str | None],
        verbose_name: str | bytes | None = ...,
        *,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True],
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
    def __get__(self, instance: Any, owner: Any) -> _C: ...
    def __set__(self, instance: Any, value: _C) -> None: ...  # type: ignore [override]
