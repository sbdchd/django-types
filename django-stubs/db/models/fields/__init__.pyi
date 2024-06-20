import decimal
import ipaddress
import uuid
from collections.abc import Callable, Iterable, Sequence
from datetime import date, datetime, time, timedelta
from typing import Any, Generic, Mapping, TypeVar, overload
from typing_extensions import Literal, Self

from django.core.checks import CheckMessage
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist
from django.db.models import Model
from django.db.models.expressions import Col, Combinable
from django.db.models.query_utils import RegisterLookupMixin
from django.forms import Widget

BLANK_CHOICE_DASH: list[tuple[str, str]] = ...

_Choice = tuple[Any, str]
_ChoiceNamedGroup = tuple[str, Iterable[_Choice]]
_ChoicesMapping = Mapping[Any, str | Mapping[Any, str]]
_LiteralFieldChoices = Iterable[_Choice | _ChoiceNamedGroup] | _ChoicesMapping
_FieldChoices = _LiteralFieldChoices | Callable[[], _LiteralFieldChoices]

_ValidatorCallable = Callable[..., None]
_ErrorMessagesToOverride = dict[str, Any]

# __set__ value type
_ST = TypeVar("_ST")
# __get__ return type
_GT = TypeVar("_GT")

class NOT_PROVIDED: ...

class Field(RegisterLookupMixin, Generic[_ST, _GT]):
    widget: Widget
    help_text: str
    db_table: str
    attname: str
    auto_created: bool
    primary_key: bool
    remote_field: Field[_ST, _GT]
    is_relation: bool
    related_model: Any | None = ...
    one_to_many: bool | None = ...
    one_to_one: bool | None = ...
    many_to_many: bool | None = ...
    many_to_one: bool | None = ...
    max_length: int
    model: type[Model]
    name: str
    verbose_name: str
    description: str
    blank: bool = ...
    null: bool = ...
    editable: bool = ...
    empty_strings_allowed: bool = ...
    choices: _FieldChoices = ...
    db_column: str | None
    db_comment: str | None
    column: str
    default: Any
    error_messages: _ErrorMessagesToOverride
    def __set__(self, instance: Any, value: _ST) -> None: ...
    # class access
    @overload
    def __get__(self, instance: None, owner: Any) -> Self: ...
    # Model instance access
    @overload
    def __get__(self, instance: Model, owner: Any) -> _GT: ...
    # non-Model instances
    @overload
    def __get__(self, instance: Any, owner: Any) -> Self: ...
    def deconstruct(self) -> Any: ...
    def set_attributes_from_name(self, name: str) -> None: ...
    def db_type(self, connection: Any) -> str: ...
    def db_parameters(self, connection: Any) -> dict[str, str]: ...
    def pre_save(self, model_instance: Model, add: bool) -> Any: ...
    def get_prep_value(self, value: Any) -> Any: ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool) -> Any: ...
    def get_db_prep_save(self, value: Any, connection: Any) -> Any: ...
    def get_internal_type(self) -> str: ...
    # TODO: plugin support
    def formfield(self, **kwargs: Any) -> Any: ...
    def save_form_data(self, instance: Model, data: Any) -> None: ...
    def contribute_to_class(
        self, cls: type[Model], name: str, private_only: bool = ...
    ) -> None: ...
    def to_python(self, value: Any) -> Any: ...
    def clean(self, value: Any, model_instance: Model | None) -> Any: ...
    def get_choices(
        self,
        include_blank: bool = ...,
        blank_choice: _Choice = ...,
        limit_choices_to: Any | None = ...,
        ordering: Sequence[str] = ...,
    ) -> Sequence[_Choice | _ChoiceNamedGroup]: ...
    def has_default(self) -> bool: ...
    def get_default(self) -> Any: ...
    def check(self, **kwargs: Any) -> list[CheckMessage]: ...
    @property
    def validators(self) -> list[_ValidatorCallable]: ...
    def validate(self, value: Any, model_instance: Model) -> None: ...
    def run_validators(self, value: Any) -> None: ...
    def get_col(
        self, alias: str, output_field: Field[Any, Any] | None = ...
    ) -> Col: ...
    @property
    def cached_col(self) -> Col: ...
    def value_from_object(self, obj: Model) -> _GT: ...
    def get_attname(self) -> str: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

_I = TypeVar("_I", bound=int | None)

class IntegerField(Generic[_I], Field[_I | Combinable, _I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> IntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> IntegerField[int | None]: ...

class PositiveIntegerRelDbTypeMixin:
    def rel_db_type(self, connection: Any) -> Any: ...

class PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> PositiveIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> PositiveIntegerField[int | None]: ...

class PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField[_I]):
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> PositiveSmallIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> PositiveSmallIntegerField[int | None]: ...

class SmallIntegerField(IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> SmallIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> SmallIntegerField[int | None]: ...

class BigIntegerField(IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> BigIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> BigIntegerField[int | None]: ...

class PositiveBigIntegerField(IntegerField[_I]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> PositiveBigIntegerField[int]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _I | Callable[[], _I] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> PositiveBigIntegerField[int | None]: ...

_F = TypeVar("_F", bound=float | None)

class FloatField(Generic[_F], Field[_F | Combinable, _F]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _F | Callable[[], _F] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_F, str] | tuple[str, Iterable[tuple[_F, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> FloatField[float]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _F | Callable[[], _F] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_F, str] | tuple[str, Iterable[tuple[_F, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> FloatField[float | None]: ...

_DEC = TypeVar("_DEC", bound=decimal.Decimal | None)

class DecimalField(Generic[_DEC], Field[_DEC | Combinable, _DEC]):
    # attributes
    max_digits: int = ...
    decimal_places: int = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _DEC | Callable[[], _DEC] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_DEC, str] | tuple[str, Iterable[tuple[_DEC, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> DecimalField[decimal.Decimal]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _DEC | Callable[[], _DEC] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_DEC, str] | tuple[str, Iterable[tuple[_DEC, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> DecimalField[decimal.Decimal | None]: ...

class AutoFieldMeta(type): ...
class AutoFieldMixin: ...

class AutoField(AutoFieldMixin, IntegerField[int], metaclass=AutoFieldMeta):
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: Literal[True] = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: int | Callable[[], int] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[int, str] | tuple[str, Iterable[tuple[int, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> Self: ...

class BigAutoField(AutoFieldMixin, BigIntegerField[int]):
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: Literal[True] = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: int | Callable[[], int] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[int, str] | tuple[str, Iterable[tuple[int, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> Self: ...

class SmallAutoField(AutoFieldMixin, SmallIntegerField[int]):
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        max_digits: int = ...,
        decimal_places: int = ...,
        primary_key: Literal[True] = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: Literal[True] = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: int | Callable[[], int] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[int, str] | tuple[str, Iterable[tuple[int, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> Self: ...

_C = TypeVar("_C", bound=str | None)

class CharField(Generic[_C], Field[_C | Combinable, _C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> CharField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> CharField[str | None]: ...

class SlugField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
        allow_unicode: bool = ...,
    ) -> SlugField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
        allow_unicode: bool = ...,
    ) -> SlugField[str | None]: ...

class EmailField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> EmailField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> EmailField[str | None]: ...

class URLField(CharField[_C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> URLField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> URLField[str | None]: ...

class TextField(Generic[_C], Field[_C | Combinable, _C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> TextField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> TextField[str | None]: ...

_B = TypeVar("_B", bound=bool | None)

class BooleanField(Generic[_B], Field[_B | Combinable, _B]):
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _B | Callable[[], _B] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_B, str] | tuple[str, Iterable[tuple[_B, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> BooleanField[bool]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        db_collation: str | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _B | Callable[[], _B] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_B, str] | tuple[str, Iterable[tuple[_B, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> BooleanField[bool | None]: ...

class IPAddressField(Generic[_C], Field[_C | Combinable, _C]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> IPAddressField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> IPAddressField[str | None]: ...

class GenericIPAddressField(
    Generic[_C],
    Field[_C | ipaddress.IPv4Address | ipaddress.IPv6Address | Combinable, _C],
):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        protocol: str = ...,
        unpack_ipv4: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> GenericIPAddressField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        protocol: str = ...,
        unpack_ipv4: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> GenericIPAddressField[str | None]: ...

_DD = TypeVar("_DD", bound=date | None)

class DateTimeCheckMixin: ...

class DateField(DateTimeCheckMixin, Field[_DD | Combinable, _DD]):
    # attributes
    auto_now: bool = ...
    auto_now_add: bool = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _DD | Callable[[], _DD] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_DD, str] | tuple[str, Iterable[tuple[_DD, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> DateField[date]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _DD | Callable[[], _DD] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_DD, str] | tuple[str, Iterable[tuple[_DD, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> DateField[date | None]: ...

_TM = TypeVar("_TM", bound=time | None)

class TimeField(Generic[_TM], DateTimeCheckMixin, Field[_TM | Combinable, _TM]):
    # attributes
    auto_now: bool = ...
    auto_now_add: bool = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _TM | Callable[[], _TM] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_TM, str] | tuple[str, Iterable[tuple[_TM, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> TimeField[time]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _TM | Callable[[], _TM] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_TM, str] | tuple[str, Iterable[tuple[_TM, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> TimeField[time | None]: ...

_DT = TypeVar("_DT", bound=datetime | None)

class DateTimeField(DateField[_DT]):
    # attributes
    auto_now: bool = ...
    auto_now_add: bool = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _DT | Callable[[], _DT] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_DT, str] | tuple[str, Iterable[tuple[_DT, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> DateTimeField[datetime]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _DT | Callable[[], _DT] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_DT, str] | tuple[str, Iterable[tuple[_DT, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> DateTimeField[datetime | None]: ...

_U = TypeVar("_U", bound=uuid.UUID | None)

class UUIDField(Generic[_U], Field[str | _U, _U]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _U | Callable[[], _U] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_U, str] | tuple[str, Iterable[tuple[_U, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> UUIDField[uuid.UUID]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _U | Callable[[], _U] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_U, str] | tuple[str, Iterable[tuple[_U, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> UUIDField[uuid.UUID | None]: ...

class FilePathField(Generic[_C], Field[_C, _C]):
    path: str | Callable[..., str] = ...
    match: str | None = ...
    recursive: bool = ...
    allow_files: bool = ...
    allow_folders: bool = ...
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        path: str | Callable[..., str] = ...,
        match: str | None = ...,
        recursive: bool = ...,
        allow_filters: bool = ...,
        allow_folders: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> FilePathField[str]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        path: str | Callable[..., str] = ...,
        match: str | None = ...,
        recursive: bool = ...,
        allow_filters: bool = ...,
        allow_folders: bool = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _C | Callable[[], _C] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_C, str] | tuple[str, Iterable[tuple[_C, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> FilePathField[str | None]: ...

_BIN = TypeVar("_BIN", bound=bytes | None)

class BinaryField(Generic[_BIN], Field[_BIN | bytearray | memoryview, _BIN]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _BIN | Callable[[], _BIN] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_BIN, str] | tuple[str, Iterable[tuple[_BIN, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> BinaryField[bytes]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _BIN | Callable[[], _BIN] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_BIN, str] | tuple[str, Iterable[tuple[_BIN, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> BinaryField[bytes | None]: ...

_TD = TypeVar("_TD", bound=timedelta | None)

class DurationField(Generic[_TD], Field[_TD, _TD]):
    @overload
    def __new__(  # type: ignore [misc]
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: _TD | Callable[[], _TD] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_TD, str] | tuple[str, Iterable[tuple[_TD, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> DurationField[timedelta]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: _TD | Callable[[], _TD] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_TD, str] | tuple[str, Iterable[tuple[_TD, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> DurationField[timedelta | None]: ...
