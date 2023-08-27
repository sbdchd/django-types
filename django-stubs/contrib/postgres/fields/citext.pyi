from collections.abc import Callable, Iterable
from typing import Any, Optional, TypeVar, Union, overload
from typing_extensions import Literal

from django.db.models.fields import CharField, EmailField, TextField

_Choice = tuple[Any, Any]
_ChoiceNamedGroup = tuple[str, Iterable[_Choice]]
_FieldChoices = Iterable[Union[_Choice, _ChoiceNamedGroup]]

_ValidatorCallable = Callable[..., None]
_ErrorMessagesToOverride = dict[str, Any]

_C = TypeVar("_C", bound="Optional[str]")

class CIText: ...

class CICharField(CIText, CharField[_C]):
    @overload
    def __init__(
        self: CICharField[str],
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: CICharField[Optional[str]],
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _C: ...
    def __set__(self, instance: Any, value: _C) -> None: ...  # type: ignore [override]

class CIEmailField(CIText, EmailField[_C]):
    @overload
    def __init__(
        self: CIEmailField[str],
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: CIEmailField[Optional[str]],
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _C: ...
    def __set__(self, instance: Any, value: _C) -> None: ...  # type: ignore [override]

class CITextField(CIText, TextField[_C]):
    @overload
    def __init__(
        self: CITextField[str],
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: CITextField[Optional[str]],
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _C: ...
    def __set__(self, instance: Any, value: _C) -> None: ...  # type: ignore [override]
