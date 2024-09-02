from collections.abc import Callable, Iterable, Sequence
from typing import Any, Generic, Protocol, TypeVar, overload
from typing_extensions import Literal, Self
from uuid import UUID

from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import Collector
from django.db.models.fields import _GT, _ST, Field
from django.db.models.fields.mixins import FieldCacheMixin
from django.db.models.fields.related_descriptors import (
    ForwardManyToOneDescriptor as ForwardManyToOneDescriptor,
)
from django.db.models.fields.related_descriptors import (  # noqa: F401
    ForwardOneToOneDescriptor as ForwardOneToOneDescriptor,
)
from django.db.models.fields.related_descriptors import (
    ManyToManyDescriptor as ManyToManyDescriptor,
)
from django.db.models.fields.related_descriptors import (
    ReverseManyToOneDescriptor as ReverseManyToOneDescriptor,
)
from django.db.models.fields.related_descriptors import (
    ReverseOneToOneDescriptor as ReverseOneToOneDescriptor,
)
from django.db.models.fields.reverse_related import (  # noqa: F401
    ForeignObjectRel as ForeignObjectRel,
)
from django.db.models.fields.reverse_related import ManyToManyRel as ManyToManyRel
from django.db.models.fields.reverse_related import ManyToOneRel as ManyToOneRel
from django.db.models.fields.reverse_related import OneToOneRel as OneToOneRel
from django.db.models.manager import ManyToManyRelatedManager
from django.db.models.query_utils import PathInfo, Q

class _DeleteProtocol(Protocol):
    def __call__(
        self,
        collector: Collector,
        field: Field[Any, Any],
        sub_objs: Sequence[Model],
        using: str,
    ) -> None: ...

_F = TypeVar("_F", bound=models.Field[Any, Any])
_Choice = tuple[Any, str]
_ChoiceNamedGroup = tuple[str, Iterable[_Choice]]
_FieldChoices = Iterable[_Choice | _ChoiceNamedGroup]
_ChoicesLimit = dict[str, Any] | Q | Callable[[], Q]
_OnDeleteOptions = _DeleteProtocol | Callable[[Any], _DeleteProtocol]

_ValidatorCallable = Callable[..., None]
_ErrorMessagesToOverride = dict[str, Any]

RECURSIVE_RELATIONSHIP_CONSTANT: str = ...

class RelatedField(FieldCacheMixin, Generic[_ST, _GT], Field[_ST, _GT]):
    one_to_many: bool = ...  # pyright: ignore[reportIncompatibleVariableOverride]
    one_to_one: bool = ...  # pyright: ignore[reportIncompatibleVariableOverride]
    many_to_many: bool = ...  # pyright: ignore[reportIncompatibleVariableOverride]
    many_to_one: bool = ...  # pyright: ignore[reportIncompatibleVariableOverride]
    related_model: type[_GT] = ...
    opts: Any = ...
    def get_forward_related_filter(self, obj: Model) -> dict[str, int | UUID]: ...
    def get_reverse_related_filter(self, obj: Model) -> Q: ...
    @property
    def swappable_setting(self) -> str | None: ...
    def set_attributes_from_rel(self) -> None: ...
    def do_related_class(self, other: type[Model], cls: type[Model]) -> None: ...
    def get_limit_choices_to(self) -> dict[str, int]: ...
    def related_query_name(self) -> str: ...
    @property
    def target_field(self) -> Field[Any, Any]: ...

_M = TypeVar("_M", bound=Model | None)

class ForeignObject(Generic[_M], RelatedField[_M, _M]):
    one_to_many: Literal[  # pyright: ignore[reportIncompatibleVariableOverride]
        False
    ] = ...
    one_to_one: Literal[  # pyright: ignore[reportIncompatibleVariableOverride]
        False
    ] = ...
    many_to_many: Literal[  # pyright: ignore[reportIncompatibleVariableOverride]
        False
    ] = ...
    many_to_one: Literal[  # pyright: ignore[reportIncompatibleVariableOverride]
        True
    ] = ...
    related_model: type[_M] = ...
    @overload
    def __new__(
        cls,
        to: type[_M] | str,
        on_delete: _OnDeleteOptions,
        from_fields: Sequence[str],
        to_fields: Sequence[str],
        *,
        rel: ForeignObjectRel | None = ...,
        related_name: str | None = ...,
        related_query_name: str | None = ...,
        limit_choices_to: _ChoicesLimit | None = ...,
        parent_link: bool = ...,
        db_constraint: bool = ...,
        swappable: bool = ...,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = False,
        db_index: bool = ...,
        default: _M | Callable[[], _M] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_M, str] | tuple[str, Iterable[tuple[_M, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> ForeignObject[_M]: ...
    @overload
    def __new__(
        cls,
        to: type[_M] | str,
        on_delete: _OnDeleteOptions,
        from_fields: Sequence[str],
        to_fields: Sequence[str],
        *,
        rel: ForeignObjectRel | None = ...,
        related_name: str | None = ...,
        related_query_name: str | None = ...,
        limit_choices_to: _ChoicesLimit | None = ...,
        parent_link: bool = ...,
        db_constraint: bool = ...,
        swappable: bool = ...,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True],
        db_index: bool = ...,
        default: _M | Callable[[], _M] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_M, str] | tuple[str, Iterable[tuple[_M, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> ForeignObject[_M | None]: ...

class ForeignKey(Generic[_M], ForeignObject[_M]):
    one_to_many: Literal[False] = ...
    one_to_one: Literal[False] = ...
    many_to_many: Literal[False] = ...
    many_to_one: Literal[True] = ...
    related_model: type[_M] = ...
    @overload
    def __new__(
        cls,
        to: type[_M] | str,
        on_delete: _OnDeleteOptions,
        *,
        to_field: str | None = ...,
        related_name: str | None = ...,
        related_query_name: str | None = ...,
        limit_choices_to: _ChoicesLimit | None = ...,
        parent_link: bool = ...,
        db_constraint: bool = ...,
        swappable: bool = ...,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = False,
        db_index: bool = ...,
        default: _M | Callable[[], _M] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_M, str] | tuple[str, Iterable[tuple[_M, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> ForeignKey[_M]: ...
    @overload
    def __new__(
        cls,
        to: type[_M] | str,
        on_delete: _OnDeleteOptions,
        *,
        to_field: str | None = ...,
        related_name: str | None = ...,
        related_query_name: str | None = ...,
        limit_choices_to: _ChoicesLimit | None = ...,
        parent_link: bool = ...,
        db_constraint: bool = ...,
        swappable: bool = ...,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True],
        db_index: bool = ...,
        default: _M | Callable[[], _M] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_M, str] | tuple[str, Iterable[tuple[_M, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> ForeignKey[_M | None]: ...
    # class access
    @overload
    def __get__(self, instance: None, owner: Any) -> ForwardManyToOneDescriptor: ...
    # Model instance access
    @overload
    def __get__(self, instance: Model, owner: Any) -> _M: ...
    # non-Model instances
    @overload
    def __get__(self, instance: Any, owner: Any) -> Self: ...

class OneToOneField(Generic[_M], ForeignKey[_M]):
    one_to_many: Literal[False] = ...
    one_to_one: Literal[True] = ...  # type: ignore [assignment]
    many_to_many: Literal[False] = ...
    many_to_one: Literal[False] = ...  # type: ignore [assignment]
    related_model: type[_M] = ...
    @overload
    def __new__(
        cls,
        to: type[_M] | str,
        on_delete: _OnDeleteOptions,
        *,
        to_field: str | None = ...,
        related_name: str | None = ...,
        related_query_name: str | None = ...,
        limit_choices_to: _ChoicesLimit | None = ...,
        parent_link: bool = ...,
        db_constraint: bool = ...,
        swappable: bool = ...,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: Literal[True] = ...,
        blank: bool = ...,
        null: Literal[False] = False,
        db_index: bool = ...,
        default: _M | Callable[[], _M] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_M, str] | tuple[str, Iterable[tuple[_M, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> OneToOneField[_M]: ...
    @overload
    def __new__(
        cls,
        to: type[_M] | str,
        on_delete: _OnDeleteOptions,
        *,
        to_field: str | None = ...,
        related_name: str | None = ...,
        related_query_name: str | None = ...,
        limit_choices_to: _ChoicesLimit | None = ...,
        parent_link: bool = ...,
        db_constraint: bool = ...,
        swappable: bool = ...,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: Literal[True] = ...,
        blank: bool = ...,
        null: Literal[True],
        db_index: bool = ...,
        default: _M | Callable[[], _M] = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_M, str] | tuple[str, Iterable[tuple[_M, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> OneToOneField[_M | None]: ...
    # class access
    @overload
    def __get__(self, instance: None, owner: Any) -> ForwardOneToOneDescriptor: ...
    # Model instance access
    @overload
    def __get__(self, instance: Model, owner: Any) -> _M: ...
    # non-Model instances
    @overload
    def __get__(self, instance: Any, owner: Any) -> Self: ...

_MM = TypeVar("_MM", bound=Model)
_MN = TypeVar("_MN", bound=Model)

class ManyToManyField(
    Generic[_MM, _MN], RelatedField[Sequence[_MN], ManyToManyRelatedManager[_MM, _MN]]
):
    one_to_many: Literal[  # pyright: ignore[reportIncompatibleVariableOverride]
        False
    ] = ...
    one_to_one: Literal[  # pyright: ignore[reportIncompatibleVariableOverride]
        False
    ] = ...
    many_to_many: Literal[  # pyright: ignore[reportIncompatibleVariableOverride]
        True
    ] = ...
    many_to_one: Literal[  # pyright: ignore[reportIncompatibleVariableOverride]
        False
    ] = ...
    rel_class: Any = ...
    description: Any = ...
    has_null_arg: Any = ...
    swappable: bool = ...
    related_model: type[_MM] = ...  # type: ignore [assignment]
    through: type[_MN]
    def __new__(
        cls,
        to: type[_MM] | str,
        through: type[_MN] | str = ...,
        to_field: str | None = ...,
        related_name: str | None = ...,
        related_query_name: str | None = ...,
        limit_choices_to: _ChoicesLimit | None = ...,
        symmetrical: bool | None = ...,
        through_fields: tuple[str, str] | None = ...,
        db_constraint: bool = ...,
        swappable: bool = ...,
        verbose_name: str | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
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
        db_table: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> Self: ...
    def get_path_info(self, filtered_relation: None = ...) -> list[PathInfo]: ...
    def get_reverse_path_info(
        self, filtered_relation: None = ...
    ) -> list[PathInfo]: ...
    def contribute_to_related_class(
        self, cls: type[Model], related: RelatedField[Any, Any]
    ) -> None: ...
    def m2m_db_table(self) -> str: ...
    def m2m_column_name(self) -> str: ...
    def m2m_reverse_name(self) -> str: ...
    def m2m_reverse_field_name(self) -> str: ...
    def m2m_target_field_name(self) -> str: ...
    def m2m_reverse_target_field_name(self) -> str: ...

def create_many_to_many_intermediary_model(
    field: type[Field[Any, Any]], klass: type[Model]
) -> type[Model]: ...
