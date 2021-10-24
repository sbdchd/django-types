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

_L = TypeVar("_L", bound=Optional[List[Any]])
_V = TypeVar("_V", bound=Optional[Union[List[Any], Any]])
_T = TypeVar("_T", bound="ArrayField[List[Any], Any]")

class ArrayField(
    CheckFieldDefaultMixin,
    Generic[_L, _V],
    Field[Union[_L, Combinable], _L],
):

    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    base_field: Field[Any, _V] = ...
    size: Optional[int] = ...
    default_validators: Any = ...
    from_db_value: Any = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        base_field: Field[Any, _V],
        *args: Any,
        null: Literal[False] = ...,
        **kwargs: Any,
    ) -> ArrayField[List[_V], _V]: ...
    @overload
    def __new__(
        cls,
        base_field: Field[Any, _V],
        *args: Any,
        null: Literal[True] = ...,
        **kwargs: Any,
    ) -> ArrayField[Optional[List[_V]], _V]: ...
    @overload
    def __init__(
        self: ArrayField[List[_V], _V],
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
        default: Optional[Union[List[_V], Callable[[], List[_V]]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[List[_V], str], Tuple[str, Iterable[Tuple[List[_V], str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: ArrayField[Optional[List[_V]], _V],
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
        default: Optional[Union[List[_V], Callable[[], List[_V]]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[List[_V], str], Tuple[str, Iterable[Tuple[List[_V], str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @property
    def description(self) -> str: ...  # type: ignore [override]
    def get_transform(self, name: Any) -> Any: ...
