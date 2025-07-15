from collections.abc import Iterable, Iterator, Mapping
from typing import Any, Literal

from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models.base import Model
from django.db.models.fields import NOT_PROVIDED, Field
from django.db.models.fields.reverse_related import ForeignObjectRel
from django.utils.functional import cached_property

StrOrPromise = str
from django.db.models.fields import Field, _LiteralFieldChoices, _ValidatorCallable

class AttributeSetter:
    def __init__(self, name: str, value: Any) -> None: ...

class CompositeAttribute:
    field: CompositePrimaryKey
    def __init__(self, field: CompositePrimaryKey) -> None: ...
    @property
    def attnames(self) -> list[str]: ...
    def __get__(
        self, instance: Model, cls: type[Model] | None = None
    ) -> tuple[Any, ...]: ...
    def __set__(
        self, instance: Model, values: list[Any] | tuple[Any] | None
    ) -> None: ...

class CompositePrimaryKey(Field[tuple[Any, ...] | None, tuple[Any, ...] | None]):
    field_names: tuple[str]
    descriptor_class: type[CompositeAttribute]
    def __init__(
        self,
        *args: str,
        verbose_name: StrOrPromise | None = None,
        name: str | None = None,
        primary_key: Literal[True] = True,
        max_length: int | None = None,
        unique: bool = False,
        blank: Literal[True] = True,
        null: bool = False,
        db_index: bool = False,
        rel: ForeignObjectRel | None = None,
        default: type[NOT_PROVIDED] = ...,
        editable: Literal[False] = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: _LiteralFieldChoices | None = None,
        help_text: StrOrPromise = "",
        db_column: None = None,
        db_tablespace: str | None = None,
        auto_created: bool = False,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: Mapping[str, StrOrPromise] | None = None,
        db_comment: str | None = None,
        db_default: type[NOT_PROVIDED] = ...,
    ) -> None: ...
    @cached_property
    def fields(
        self,
    ) -> tuple[Field[Any, Any] | ForeignObjectRel | GenericForeignKey, ...]: ...
    @cached_property
    def columns(self) -> tuple[str, ...]: ...
    def __iter__(
        self,
    ) -> Iterator[Field[Any, Any] | ForeignObjectRel | GenericForeignKey]: ...
    def __len__(self) -> int: ...
    def get_pk_value_on_save(
        self, instance: Model
    ) -> tuple[Any, ...] | None: ...  # actual type is tuple of field.value_from_object

def unnest(fields: Iterable[Field[Any, Any]]) -> list[Field[Any, Any]]: ...
