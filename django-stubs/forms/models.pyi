from collections.abc import (
    Callable,
    Container,
    Iterator,
    Mapping,
    MutableMapping,
    Sequence,
)
from datetime import datetime
from typing import Any, ClassVar, Optional, TypeVar, Union
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

_Fields = Union[list[Union[Callable[..., Any], str]], Sequence[str], Literal["__all__"]]
_Labels = dict[str, str]
_ErrorMessages = dict[str, dict[str, str]]

_M = TypeVar("_M", bound=Model)

def construct_instance(
    form: BaseForm,
    instance: _M,
    fields: Optional[Container[str]] = ...,
    exclude: Optional[Container[str]] = ...,
) -> _M: ...
def model_to_dict(
    instance: Model, fields: Optional[_Fields] = ..., exclude: Optional[_Fields] = ...
) -> dict[str, Any]: ...
def fields_for_model(
    model: type[Model],
    fields: Optional[_Fields] = ...,
    exclude: Optional[_Fields] = ...,
    widgets: Optional[Union[dict[str, type[Input]], dict[str, Widget]]] = ...,
    formfield_callback: Optional[Union[Callable[..., Any], str]] = ...,
    localized_fields: Optional[Union[tuple[str], str]] = ...,
    labels: Optional[_Labels] = ...,
    help_texts: Optional[dict[str, str]] = ...,
    error_messages: Optional[_ErrorMessages] = ...,
    field_classes: Optional[dict[str, type[CharField]]] = ...,
    *,
    apply_limit_choices_to: bool = ...
) -> dict[str, Any]: ...

class ModelFormOptions:
    model: Optional[type[Model]] = ...
    fields: Optional[_Fields] = ...
    exclude: Optional[_Fields] = ...
    widgets: Optional[dict[str, Union[Widget, Input]]] = ...
    localized_fields: Optional[Union[tuple[str], str]] = ...
    labels: Optional[_Labels] = ...
    help_texts: Optional[dict[str, str]] = ...
    error_messages: Optional[_ErrorMessages] = ...
    field_classes: Optional[dict[str, type[Field]]] = ...
    def __init__(self, options: Optional[type] = ...) -> None: ...

class ModelFormMetaclass(DeclarativeFieldsMetaclass): ...

class BaseModelForm(BaseForm):
    instance: Any = ...
    def __init__(
        self,
        data: Optional[Mapping[str, Any]] = ...,
        files: Optional[Mapping[str, File]] = ...,
        auto_id: Union[bool, str] = ...,
        prefix: Optional[str] = ...,
        initial: Optional[dict[str, Any]] = ...,
        error_class: type[ErrorList] = ...,
        label_suffix: Optional[str] = ...,
        empty_permitted: bool = ...,
        instance: Optional[Model] = ...,
        use_required_attribute: Optional[bool] = ...,
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
    fields: Optional[_Fields] = ...,
    exclude: Optional[_Fields] = ...,
    formfield_callback: Optional[
        Union[str, Callable[[models.Field[Any, Any]], Field]]
    ] = ...,
    widgets: Optional[MutableMapping[str, Widget]] = ...,
    localized_fields: Optional[Sequence[str]] = ...,
    labels: Optional[MutableMapping[str, str]] = ...,
    help_texts: Optional[MutableMapping[str, str]] = ...,
    error_messages: Optional[MutableMapping[str, dict[str, Any]]] = ...,
    field_classes: Optional[MutableMapping[str, type[Field]]] = ...,
) -> type[ModelForm]: ...

class BaseModelFormSet(BaseFormSet):
    model: Any = ...
    unique_fields: Any = ...
    queryset: Any = ...
    initial_extra: Any = ...
    def __init__(
        self,
        data: Optional[Any] = ...,
        files: Optional[Any] = ...,
        auto_id: str = ...,
        prefix: Optional[Any] = ...,
        queryset: Optional[Any] = ...,
        *,
        initial: Optional[Any] = ...,
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
    formfield_callback: Optional[Callable[..., Any]] = ...,
    formset: type[BaseModelFormSet] = ...,
    extra: int = ...,
    can_delete: bool = ...,
    can_order: bool = ...,
    min_num: Optional[int] = ...,
    max_num: Optional[int] = ...,
    fields: Optional[_Fields] = ...,
    exclude: Optional[_Fields] = ...,
    widgets: Optional[dict[str, Any]] = ...,
    validate_max: bool = ...,
    localized_fields: Optional[Sequence[str]] = ...,
    labels: Optional[dict[str, str]] = ...,
    help_texts: Optional[dict[str, str]] = ...,
    error_messages: Optional[dict[str, dict[str, str]]] = ...,
    validate_min: bool = ...,
    field_classes: Optional[dict[str, type[Field]]] = ...,
) -> type[BaseModelFormSet]: ...

class BaseInlineFormSet(BaseModelFormSet):
    instance: Any = ...
    save_as_new: Any = ...
    unique_fields: Any = ...
    def __init__(
        self,
        data: Optional[Any] = ...,
        files: Optional[Any] = ...,
        instance: Optional[Any] = ...,
        save_as_new: bool = ...,
        prefix: Optional[Any] = ...,
        queryset: Optional[Any] = ...,
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
    fk_name: Optional[str] = ...,
    fields: Optional[_Fields] = ...,
    exclude: Optional[_Fields] = ...,
    extra: int = ...,
    can_order: bool = ...,
    can_delete: bool = ...,
    max_num: Optional[int] = ...,
    formfield_callback: Optional[Callable[..., Any]] = ...,
    widgets: Optional[dict[str, Any]] = ...,
    validate_max: bool = ...,
    localized_fields: Optional[Sequence[str]] = ...,
    labels: Optional[dict[str, str]] = ...,
    help_texts: Optional[dict[str, str]] = ...,
    error_messages: Optional[dict[str, dict[str, str]]] = ...,
    min_num: Optional[int] = ...,
    validate_min: bool = ...,
    field_classes: Optional[dict[str, Any]] = ...,
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
    to_field: Optional[str] = ...
    def __init__(
        self,
        parent_instance: Model,
        *args: Any,
        pk_field: bool = ...,
        to_field: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...

class ModelChoiceIterator:
    field: ModelChoiceField = ...
    queryset: Optional[QuerySet[Any]] = ...
    def __init__(self, field: ModelChoiceField) -> None: ...
    def __iter__(self) -> Iterator[tuple[Union[int, str], str]]: ...
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
    empty_label: Optional[str] = ...
    queryset: Any = ...
    limit_choices_to: Optional[Union[dict[str, Any], Callable[[], Any]]] = ...
    to_field_name: None = ...
    def __init__(
        self,
        queryset: Optional[Union[Manager[Any], QuerySet[Any]]],
        *,
        empty_label: Optional[str] = ...,
        required: bool = ...,
        widget: Optional[Any] = ...,
        label: Optional[Any] = ...,
        initial: Optional[Any] = ...,
        help_text: str = ...,
        to_field_name: Optional[Any] = ...,
        limit_choices_to: Optional[Union[dict[str, Any], Callable[[], Any]]] = ...,
        **kwargs: Any
    ) -> None: ...
    def get_limit_choices_to(
        self,
    ) -> Optional[Union[dict[str, datetime], Q, MagicMock]]: ...
    def label_from_instance(self, obj: Model) -> str: ...
    choices: Any = ...
    def validate(self, value: Optional[Model]) -> None: ...
    def has_changed(
        self,
        initial: Optional[Union[Model, int, str, UUID]],
        data: Optional[Union[int, str]],
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
    fk_name: Optional[str] = ...,
    can_fail: bool = ...,
) -> ForeignKey[Any]: ...
