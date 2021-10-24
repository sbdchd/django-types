import decimal
import ipaddress
import uuid
from datetime import date, datetime, time, timedelta
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from django.core.checks import CheckMessage
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist
from django.db.models import Model
from django.db.models.expressions import Col, Combinable
from django.db.models.query_utils import RegisterLookupMixin
from django.forms import Field as FormField
from django.forms import Widget
from typing_extensions import Literal

class NOT_PROVIDED: ...

BLANK_CHOICE_DASH: List[Tuple[str, str]] = ...

_Choice = Tuple[Any, str]
_ChoiceNamedGroup = Tuple[str, Iterable[_Choice]]
_FieldChoices = Iterable[Union[_Choice, _ChoiceNamedGroup]]

_ValidatorCallable = Callable[..., None]
_ErrorMessagesToOverride = Dict[str, Any]

_T = TypeVar("_T", bound="Field[Any, Any]")
# __set__ value type
_ST = TypeVar("_ST", contravariant=True)
# __get__ return type
_GT = TypeVar("_GT", covariant=True)

class Field(RegisterLookupMixin, Generic[_ST, _GT]):

    widget: Widget
    help_text: str
    db_table: str
    attname: str
    auto_created: bool
    primary_key: bool
    remote_field: Field[_ST, _GT]
    is_relation: bool
    related_model: Any
    one_to_many: Optional[bool] = ...
    one_to_one: Optional[bool] = ...
    many_to_many: Optional[bool] = ...
    many_to_one: Optional[bool] = ...
    max_length: int
    model: Type[Model]
    name: str
    verbose_name: str
    description: str
    blank: bool = ...
    null: bool = ...
    editable: bool = ...
    empty_strings_allowed: bool = ...
    choices: _FieldChoices = ...
    db_column: Optional[str]
    column: str
    default: Any
    error_messages: _ErrorMessagesToOverride
    def __set__(self, instance: Any, value: _ST) -> None: ...
    # class access
    @overload
    def __get__(self: _T, instance: None, owner: Any) -> _T: ...
    # Model instance access
    @overload
    def __get__(self, instance: Model, owner: Any) -> _GT: ...
    # non-Model instances
    @overload
    def __get__(self: _T, instance: Any, owner: Any) -> _T: ...
    def deconstruct(self) -> Any: ...
    def set_attributes_from_name(self, name: str) -> None: ...
    def db_type(self, connection: Any) -> str: ...
    def db_parameters(self, connection: Any) -> Dict[str, str]: ...
    def pre_save(self, model_instance: Model, add: bool) -> Any: ...
    def get_prep_value(self, value: Any) -> Any: ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool) -> Any: ...
    def get_db_prep_save(self, value: Any, connection: Any) -> Any: ...
    def get_internal_type(self) -> str: ...
    # TODO: plugin support
    def formfield(self, **kwargs: Any) -> Any: ...
    def save_form_data(self, instance: Model, data: Any) -> None: ...
    def contribute_to_class(
        self, cls: Type[Model], name: str, private_only: bool = ...
    ) -> None: ...
    def to_python(self, value: Any) -> Any: ...
    def clean(self, value: Any, model_instance: Optional[Model]) -> Any: ...
    def get_choices(
        self,
        include_blank: bool = ...,
        blank_choice: _Choice = ...,
        limit_choices_to: Optional[Any] = ...,
        ordering: Sequence[str] = ...,
    ) -> Sequence[Union[_Choice, _ChoiceNamedGroup]]: ...
    def has_default(self) -> bool: ...
    def get_default(self) -> Any: ...
    def check(self, **kwargs: Any) -> List[CheckMessage]: ...
    @property
    def validators(self) -> List[_ValidatorCallable]: ...
    def validate(self, value: Any, model_instance: Model) -> None: ...
    def run_validators(self, value: Any) -> None: ...
    def get_col(
        self, alias: str, output_field: Optional[Field[Any, Any]] = ...
    ) -> Col: ...
    @property
    def cached_col(self) -> Col: ...
    def value_from_object(self, obj: Model) -> _GT: ...
    def get_attname(self) -> str: ...
    @overload
    def __init__(
        self: Field[_ST, _GT],
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
    ) -> None: ...
    @overload
    def __init__(
        self: Field[Optional[_ST], Optional[_GT]],
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
    ) -> None: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> Field[_ST, _GT]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> Field[Optional[_ST], Optional[_GT]]: ...

_I = TypeVar("_I", bound=Optional[int])

class IntegerField(Generic[_I], Field[Union[_I, Combinable], _I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> IntegerField[int]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> IntegerField[Optional[int]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> IntegerField[_I]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> IntegerField[Optional[_I]]: ...

class PositiveIntegerRelDbTypeMixin:
    def rel_db_type(self, connection: Any) -> Any: ...

class PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> PositiveIntegerField[int]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> PositiveIntegerField[Optional[int]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> PositiveIntegerField[_I]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> PositiveIntegerField[Optional[_I]]: ...

class PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> PositiveSmallIntegerField[int]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> PositiveSmallIntegerField[Optional[int]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> PositiveSmallIntegerField[_I]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> PositiveSmallIntegerField[Optional[_I]]: ...

class SmallIntegerField(IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> SmallIntegerField[int]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> SmallIntegerField[Optional[int]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> SmallIntegerField[_I]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> SmallIntegerField[Optional[_I]]: ...

class BigIntegerField(IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> BigIntegerField[int]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> BigIntegerField[Optional[int]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> BigIntegerField[_I]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> BigIntegerField[Optional[_I]]: ...

class PositiveBigIntegerField(IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> PositiveBigIntegerField[int]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> PositiveBigIntegerField[Optional[int]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> PositiveBigIntegerField[_I]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_I, str], Tuple[str, Iterable[Tuple[_I, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> PositiveBigIntegerField[Optional[_I]]: ...

_F = TypeVar("_F", bound=Optional[float])

class FloatField(Generic[_F], Field[Union[_F, Combinable], _F]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> FloatField[float]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> FloatField[Optional[float]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_F, str], Tuple[str, Iterable[Tuple[_F, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> FloatField[_F]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_F, str], Tuple[str, Iterable[Tuple[_F, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> FloatField[Optional[_F]]: ...

_DEC = TypeVar("_DEC", bound=Optional[decimal.Decimal])

class DecimalField(Generic[_DEC], Field[Union[_DEC, Combinable], _DEC]):
    # attributes
    max_digits: int = ...
    decimal_places: int = ...
    @overload
    def __init__(
        self: DecimalField[decimal.Decimal],
        max_digits: int,
        decimal_places: int,
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
    ) -> None: ...
    @overload
    def __init__(
        self: DecimalField[Optional[decimal.Decimal]],
        max_digits: int,
        decimal_places: int,
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
    ) -> None: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> DecimalField[decimal.Decimal]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> DecimalField[Optional[decimal.Decimal]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_F, str], Tuple[str, Iterable[Tuple[_F, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> DecimalField[_DEC]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_F, str], Tuple[str, Iterable[Tuple[_F, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> DecimalField[Optional[_DEC]]: ...

class AutoFieldMeta(type): ...
class AutoFieldMixin: ...

class AutoField(AutoFieldMixin, IntegerField[Optional[int]], metaclass=AutoFieldMeta):
    pass

class BigAutoField(AutoFieldMixin, BigIntegerField[Optional[int]]):
    pass

class SmallAutoField(AutoFieldMixin, SmallIntegerField[Optional[int]]):
    pass

_C = TypeVar("_C", bound=Optional[str])

class CharField(Generic[_C], Field[Union[_C, Combinable], _C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> CharField[str]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> CharField[Optional[str]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> CharField[_C]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> CharField[Optional[_C]]: ...

class SlugField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> SlugField[str]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> SlugField[Optional[str]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> SlugField[_C]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> SlugField[Optional[_C]]: ...

class EmailField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> EmailField[str]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> EmailField[Optional[str]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> EmailField[_C]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> EmailField[Optional[_C]]: ...

class URLField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> URLField[str]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> URLField[Optional[str]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> URLField[_C]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> URLField[Optional[_C]]: ...

class TextField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> TextField[str]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> TextField[Optional[str]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> TextField[_C]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> TextField[Optional[_C]]: ...

_B = TypeVar("_B", bound=Optional[bool])

class BooleanField(Generic[_B], Field[Union[_B, Combinable], _B]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> BooleanField[bool]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> BooleanField[Optional[bool]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> BooleanField[_B]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> BooleanField[Optional[_B]]: ...

class IPAddressField(Generic[_C], Field[Union[_C, Combinable], _C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> IPAddressField[str]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> IPAddressField[Optional[str]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> IPAddressField[_C]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> IPAddressField[Optional[_C]]: ...

class GenericIPAddressField(
    Generic[_C],
    Field[Union[_C, ipaddress.IPv4Address, ipaddress.IPv6Address, Combinable], _C],
):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> GenericIPAddressField[str]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> GenericIPAddressField[Optional[str]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> GenericIPAddressField[_C]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> GenericIPAddressField[Optional[_C]]: ...

_DD = TypeVar("_DD", bound=Optional[date])

class DateTimeCheckMixin: ...

class DateField(DateTimeCheckMixin, Field[Union[_DD, Combinable], _DD]):
    # attributes
    auto_now: bool = ...
    auto_now_add: bool = ...
    @overload
    def __init__(
        self: DateField[date],
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_DD, Callable[[], _DD]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DD, str], Tuple[str, Iterable[Tuple[_DD, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DateField[Optional[date]],
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Optional[Union[_DD, Callable[[], _DD]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DD, str], Tuple[str, Iterable[Tuple[_DD, str]]]]
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
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> DateField[date]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> DateField[Optional[date]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_DD, str], Tuple[str, Iterable[Tuple[_DD, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> DateField[_DD]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_DD, str], Tuple[str, Iterable[Tuple[_DD, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> DateField[Optional[_DD]]: ...

_TM = TypeVar("_TM", bound=Optional[time])

class TimeField(Generic[_TM], DateTimeCheckMixin, Field[Union[_TM, Combinable], _TM]):
    # attributes
    auto_now: bool = ...
    auto_now_add: bool = ...
    @overload
    def __init__(
        self: TimeField[time],
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_TM, Callable[[], _TM]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_TM, str], Tuple[str, Iterable[Tuple[_TM, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: TimeField[Optional[time]],
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Optional[Union[_TM, Callable[[], _TM]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_TM, str], Tuple[str, Iterable[Tuple[_TM, str]]]]
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
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> TimeField[time]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> TimeField[Optional[time]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_TM, str], Tuple[str, Iterable[Tuple[_TM, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> TimeField[_TM]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_TM, str], Tuple[str, Iterable[Tuple[_TM, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> TimeField[Optional[_TM]]: ...

_DT = TypeVar("_DT", bound=Optional[datetime])

class DateTimeField(
    Generic[_DT], DateTimeCheckMixin, Field[Union[str, datetime], datetime]
):
    # attributes
    auto_now: bool = ...
    auto_now_add: bool = ...
    @overload
    def __init__(
        self: DateTimeField[datetime],
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_DT, Callable[[], _DT]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DT, str], Tuple[str, Iterable[Tuple[_DT, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DateTimeField[Optional[datetime]],
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Optional[Union[_DT, Callable[[], _DT]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_DT, str], Tuple[str, Iterable[Tuple[_DT, str]]]]
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
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> DateTimeField[datetime]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> DateTimeField[Optional[datetime]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_DT, str], Tuple[str, Iterable[Tuple[_DT, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> DateTimeField[_DT]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_DT, str], Tuple[str, Iterable[Tuple[_DT, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> DateTimeField[Optional[_DT]]: ...

_U = TypeVar("_U", bound=Optional[uuid.UUID])

class UUIDField(Generic[_U], Field[Union[str, _U], _U]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> UUIDField[uuid.UUID]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> UUIDField[Optional[uuid.UUID]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_U, str], Tuple[str, Iterable[Tuple[_U, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> UUIDField[_U]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_U, str], Tuple[str, Iterable[Tuple[_U, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> UUIDField[Optional[_U]]: ...

class FilePathField(Generic[_C], Field[_C, _C]):
    path: Union[str, Callable[..., str]] = ...
    match: Optional[str] = ...
    recursive: bool = ...
    allow_files: bool = ...
    allow_folders: bool = ...
    @overload
    def __init__(
        self: FilePathField[str],
        path: Union[str, Callable[..., str]] = ...,
        match: Optional[str] = ...,
        recursive: bool = ...,
        allow_files: bool = ...,
        allow_folders: bool = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: FilePathField[Optional[str]],
        path: Union[str, Callable[..., str]] = ...,
        match: Optional[str] = ...,
        recursive: bool = ...,
        allow_files: bool = ...,
        allow_folders: bool = ...,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Optional[Union[_C, Callable[[], _C]]] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
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
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> FilePathField[str]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> FilePathField[Optional[str]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> FilePathField[_C]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_C, str], Tuple[str, Iterable[Tuple[_C, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> FilePathField[Optional[_C]]: ...

_BIN = TypeVar("_BIN", bound=Optional[bytes])

class BinaryField(Generic[_BIN], Field[Union[_BIN, bytearray, memoryview], _BIN]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> BinaryField[bytes]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> BinaryField[Optional[bytes]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_BIN, str], Tuple[str, Iterable[Tuple[_BIN, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> BinaryField[_BIN]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_BIN, str], Tuple[str, Iterable[Tuple[_BIN, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> BinaryField[Optional[_BIN]]: ...

_TD = TypeVar("_TD", bound=Optional[timedelta])

class DurationField(Generic[_TD], Field[_TD, _TD]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> DurationField[timedelta]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: None = ...,
        **kwargs: Any,
    ) -> DurationField[Optional[timedelta]]: ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        *args: Any,
        null: Literal[False] = ...,
        choices: Iterable[
            Union[Tuple[_TD, str], Tuple[str, Iterable[Tuple[_TD, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> DurationField[_TD]: ...
    @overload
    def __new__(
        cls,
        *args: Any,
        null: Literal[True] = ...,
        choices: Iterable[
            Union[Tuple[_TD, str], Tuple[str, Iterable[Tuple[_TD, str]]]]
        ] = ...,
        **kwargs: Any,
    ) -> DurationField[Optional[_TD]]: ...
