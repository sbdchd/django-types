from collections.abc import (
    Callable,
    Container,
    Iterator,
    Mapping,
    MutableMapping,
    Sequence,
)
from datetime import datetime
from typing import Any, ClassVar, TypeVar
from typing_extensions import Literal
from unittest.mock import MagicMock
from uuid import UUID

from django.core.files.base import File
from django.db import models
from django.db.models import ForeignKey
from django.db.models.base import Model
from django.db.models.manager import Manager
from django.db.models.query import QuerySet, _BaseQuerySet
from django.db.models.query_utils import Q
from django.forms.fields import CharField, ChoiceField, Field
from django.forms.forms import BaseForm, DeclarativeFieldsMetaclass
from django.forms.formsets import BaseFormSet
from django.forms.utils import ErrorList
from django.forms.widgets import Input, Widget

ALL_FIELDS: str

_Fields = list[Callable[..., Any] | str] | Sequence[str] | Literal["__all__"]
_Labels = dict[str, str]
_ErrorMessages = dict[str, dict[str, str]]

_M = TypeVar("_M", bound=Model)

def construct_instance(
    form: BaseForm,
    instance: _M,
    fields: Container[str] | None = ...,
    exclude: Container[str] | None = ...,
) -> _M: ...
def model_to_dict(
    instance: Model, fields: _Fields | None = ..., exclude: _Fields | None = ...
) -> dict[str, Any]: ...
def fields_for_model(
    model: type[Model],
    fields: _Fields | None = ...,
    exclude: _Fields | None = ...,
    widgets: dict[str, type[Input]] | dict[str, Widget] | None = ...,
    formfield_callback: Callable[..., Any] | str | None = ...,
    localized_fields: tuple[str] | str | None = ...,
    labels: _Labels | None = ...,
    help_texts: dict[str, str] | None = ...,
    error_messages: _ErrorMessages | None = ...,
    field_classes: dict[str, type[CharField]] | None = ...,
    *,
    apply_limit_choices_to: bool = ...
) -> dict[str, Any]: ...

class ModelFormOptions:
    model: type[Model] | None = ...
    fields: _Fields | None = ...
    exclude: _Fields | None = ...
    widgets: dict[str, Widget | Input] | None = ...
    localized_fields: tuple[str] | str | None = ...
    labels: _Labels | None = ...
    help_texts: dict[str, str] | None = ...
    error_messages: _ErrorMessages | None = ...
    field_classes: dict[str, type[Field]] | None = ...
    def __init__(self, options: type | None = ...) -> None: ...

class ModelFormMetaclass(DeclarativeFieldsMetaclass): ...

class BaseModelForm(BaseForm):
    instance: Any = ...
    def __init__(
        self,
        data: Mapping[str, Any] | None = ...,
        files: Mapping[str, File] | None = ...,
        auto_id: bool | str = ...,
        prefix: str | None = ...,
        initial: dict[str, Any] | None = ...,
        error_class: type[ErrorList] = ...,
        label_suffix: str | None = ...,
        empty_permitted: bool = ...,
        instance: Model | None = ...,
        use_required_attribute: bool | None = ...,
        renderer: Any = ...,
    ) -> None: ...
    def validate_unique(self) -> None: ...
    save_m2m: Any = ...
    def save(self, commit: bool = ...) -> Any: ...

class ModelForm(BaseModelForm, metaclass=ModelFormMetaclass):
    base_fields: ClassVar[dict[str, Field]] = ...

def modelform_factory(
    model: type[Model],
    form: type[ModelForm] = ...,
    fields: _Fields | None = ...,
    exclude: _Fields | None = ...,
    formfield_callback: str | Callable[[models.Field[Any, Any]], Field] | None = ...,
    widgets: MutableMapping[str, Widget] | None = ...,
    localized_fields: Sequence[str] | None = ...,
    labels: MutableMapping[str, str] | None = ...,
    help_texts: MutableMapping[str, str] | None = ...,
    error_messages: MutableMapping[str, dict[str, Any]] | None = ...,
    field_classes: MutableMapping[str, type[Field]] | None = ...,
) -> type[ModelForm]: ...

class BaseModelFormSet(BaseFormSet):
    model: Any = ...
    unique_fields: Any = ...
    queryset: Any = ...
    initial_extra: Any = ...
    def __init__(
        self,
        data: Any | None = ...,
        files: Any | None = ...,
        auto_id: str = ...,
        prefix: Any | None = ...,
        queryset: Any | None = ...,
        *,
        initial: Any | None = ...,
        **kwargs: Any
    ) -> None: ...
    def initial_form_count(self) -> Any: ...
    def get_queryset(self) -> Any: ...
    def save_new(self, form: Any, commit: bool = ...) -> Any: ...
    def save_existing(self, form: Any, instance: Any, commit: bool = ...) -> Any: ...
    def delete_existing(self, obj: Any, commit: bool = ...) -> None: ...
    saved_forms: Any = ...
    save_m2m: Any = ...
    def save(self, commit: bool = ...) -> Any: ...
    def clean(self) -> None: ...
    def validate_unique(self) -> None: ...
    def get_unique_error_message(self, unique_check: Any) -> Any: ...
    def get_date_error_message(self, date_check: Any) -> Any: ...
    def get_form_error(self) -> Any: ...
    changed_objects: Any = ...
    deleted_objects: Any = ...
    def save_existing_objects(self, commit: bool = ...) -> Any: ...
    new_objects: Any = ...
    def save_new_objects(self, commit: bool = ...) -> Any: ...
    def add_fields(self, form: Any, index: Any) -> Any: ...

def modelformset_factory(
    model: type[Model],
    form: type[ModelForm] = ...,
    formfield_callback: Callable[..., Any] | None = ...,
    formset: type[BaseModelFormSet] = ...,
    extra: int = ...,
    can_delete: bool = ...,
    can_order: bool = ...,
    min_num: int | None = ...,
    max_num: int | None = ...,
    fields: _Fields | None = ...,
    exclude: _Fields | None = ...,
    widgets: dict[str, Any] | None = ...,
    validate_max: bool = ...,
    localized_fields: Sequence[str] | None = ...,
    labels: dict[str, str] | None = ...,
    help_texts: dict[str, str] | None = ...,
    error_messages: dict[str, dict[str, str]] | None = ...,
    validate_min: bool = ...,
    field_classes: dict[str, type[Field]] | None = ...,
) -> type[BaseModelFormSet]: ...

class BaseInlineFormSet(BaseModelFormSet):
    instance: Any = ...
    save_as_new: Any = ...
    unique_fields: Any = ...
    def __init__(
        self,
        data: Any | None = ...,
        files: Any | None = ...,
        instance: Any | None = ...,
        save_as_new: bool = ...,
        prefix: Any | None = ...,
        queryset: Any | None = ...,
        **kwargs: Any
    ) -> None: ...
    def initial_form_count(self) -> Any: ...
    @classmethod
    def get_default_prefix(cls) -> Any: ...
    def save_new(self, form: Any, commit: bool = ...) -> Any: ...
    def add_fields(self, form: Any, index: Any) -> None: ...
    def get_unique_error_message(self, unique_check: Any) -> Any: ...

def inlineformset_factory(
    parent_model: type[Model],
    model: type[Model],
    form: type[ModelForm] = ...,
    formset: type[BaseInlineFormSet] = ...,
    fk_name: str | None = ...,
    fields: _Fields | None = ...,
    exclude: _Fields | None = ...,
    extra: int = ...,
    can_order: bool = ...,
    can_delete: bool = ...,
    max_num: int | None = ...,
    formfield_callback: Callable[..., Any] | None = ...,
    widgets: dict[str, Any] | None = ...,
    validate_max: bool = ...,
    localized_fields: Sequence[str] | None = ...,
    labels: dict[str, str] | None = ...,
    help_texts: dict[str, str] | None = ...,
    error_messages: dict[str, dict[str, str]] | None = ...,
    min_num: int | None = ...,
    validate_min: bool = ...,
    field_classes: dict[str, Any] | None = ...,
) -> type[BaseInlineFormSet]: ...

class InlineForeignKeyField(Field):
    disabled: bool
    help_text: str
    required: bool
    show_hidden_initial: bool
    widget: Any = ...
    default_error_messages: Any = ...
    parent_instance: Model = ...
    pk_field: bool = ...
    to_field: str | None = ...
    def __init__(
        self,
        parent_instance: Model,
        *args: Any,
        pk_field: bool = ...,
        to_field: Any | None = ...,
        **kwargs: Any
    ) -> None: ...

class ModelChoiceIterator:
    field: ModelChoiceField = ...
    queryset: QuerySet[Any] | None = ...
    def __init__(self, field: ModelChoiceField) -> None: ...
    def __iter__(self) -> Iterator[tuple[int | str, str]]: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def choice(self, obj: Model) -> tuple[int, str]: ...

class ModelChoiceField(ChoiceField):
    disabled: bool
    error_messages: dict[str, str]
    help_text: str
    required: bool
    show_hidden_initial: bool
    validators: list[Any]
    default_error_messages: Any = ...
    iterator: Any = ...
    empty_label: str | None = ...
    queryset: Any = ...
    limit_choices_to: dict[str, Any] | Callable[[], Any] | None = ...
    to_field_name: None = ...
    def __init__(
        self,
        queryset: Manager[Any] | QuerySet[Any] | None,
        *,
        empty_label: str | None = ...,
        required: bool = ...,
        widget: Any | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        to_field_name: Any | None = ...,
        limit_choices_to: dict[str, Any] | Callable[[], Any] | None = ...,
        **kwargs: Any
    ) -> None: ...
    def get_limit_choices_to(
        self,
    ) -> dict[str, datetime] | Q | MagicMock | None: ...
    def label_from_instance(self, obj: Model) -> str: ...
    choices: Any = ...
    def validate(self, value: Model | None) -> None: ...
    def has_changed(
        self,
        initial: Model | int | str | UUID | None,
        data: int | str | None,
    ) -> bool: ...

class ModelMultipleChoiceField(ModelChoiceField):
    disabled: bool
    empty_label: None
    help_text: str
    required: bool
    show_hidden_initial: bool
    widget: Any = ...
    hidden_widget: Any = ...
    default_error_messages: Any = ...
    def __init__(self, queryset: _BaseQuerySet[Any], **kwargs: Any) -> None: ...

def _get_foreign_key(
    parent_model: type[Model],
    model: type[Model],
    fk_name: str | None = ...,
    can_fail: bool = ...,
) -> ForeignKey[Any]: ...
