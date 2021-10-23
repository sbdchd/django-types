from typing import (
    Any,
    Callable,
    Generic,
    Iterable,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    overload,
)

from django.db.models.expressions import Combinable
from django.db.models.fields import Field, _ErrorMessagesToOverride, _ValidatorCallable
from typing_extensions import Literal

from .mixins import CheckFieldDefaultMixin

_GV = TypeVar("_GV", bound=Optional[Any])
_SV = TypeVar("_SV", bound=Optional[Any])
_ST = TypeVar("_ST", bound=Optional[Union[List[Any], Any]])
_GT = TypeVar("_GT", bound=Optional[Union[List[Any], Any]])

class ArrayField(
    CheckFieldDefaultMixin,
    Generic[_SV, _GV, _ST, _GT],
    Field[Union[_SV, Combinable], _GV],
):

    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    base_field: Field[_ST, _GT] = ...
    size: Optional[int] = ...
    default_validators: Any = ...
    from_db_value: Any = ...
    def __init__(
        self: ArrayField[List[_ST], List[_GT], List[_ST], List[_GT]],
        base_field: Field[_ST, _GT],
        size: Optional[int] = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Optional[Union[_GT, Callable[[], _GT]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_GT, str], Tuple[str, Iterable[Tuple[_GT, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        base_field: Field[_ST, _GT],
        size: Optional[int] = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_GT, Callable[[], _GT]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_GT, str], Tuple[str, Iterable[Tuple[_GT, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> ArrayField[List[_ST], List[_GT], List[_ST], List[_GT]]: ...
    @overload
    def __new__(
        cls,
        base_field: Field[_ST, _GT],
        size: Optional[int] = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Optional[Union[_GT, Callable[[], _GT]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_GT, str], Tuple[str, Iterable[Tuple[_GT, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> ArrayField[
        Optional[List[_ST]],
        Optional[List[_GT]],
        Optional[List[_ST]],
        Optional[List[_GT]],
    ]: ...
    # class access
    def __set__(self, instance: Any, value: _GV) -> None: ...  # type: ignore [override]
    @property
    def description(self) -> str: ...  # type: ignore [override]
    def get_transform(self, name: Any) -> Any: ...
