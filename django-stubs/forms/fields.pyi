from collections.abc import Callable, Iterable, Sequence
from datetime import datetime, timedelta
from re import Pattern
from typing import Any

from django.core.validators import BaseValidator
from django.forms.boundfield import BoundField
from django.forms.forms import BaseForm
from django.forms.widgets import Widget

_Choice = tuple[Any, str]
_ChoiceNamedGroup = tuple[str, Iterable[_Choice]]
_FieldChoices = Iterable[_Choice | _ChoiceNamedGroup]

class Field:
    initial: Any
    label: str | None
    required: bool
    widget: type[Widget] | Widget = ...
    hidden_widget: Any = ...
    default_validators: Any = ...
    default_error_messages: Any = ...
    empty_values: Any = ...
    show_hidden_initial: bool = ...
    help_text: str = ...
    disabled: bool = ...
    label_suffix: Any | None = ...
    localize: bool = ...
    error_messages: Any = ...
    validators: list[BaseValidator] = ...
    max_length: int | str | None = ...
    choices: _FieldChoices = ...
    base_field: Field
    def __init__(
        self,
        *,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...
    def prepare_value(self, value: Any) -> Any: ...
    def to_python(self, value: Any | None) -> Any | None: ...
    def validate(self, value: Any) -> None: ...
    def run_validators(self, value: Any) -> None: ...
    def clean(self, value: Any) -> Any: ...
    def bound_data(self, data: Any, initial: Any) -> Any: ...
    def widget_attrs(self, widget: Widget) -> Any: ...
    def has_changed(self, initial: Any, data: Any) -> bool: ...
    def get_bound_field(self, form: BaseForm, field_name: str) -> BoundField: ...
    def deconstruct(self) -> Any: ...

class CharField(Field):
    min_length: int | str | None = ...
    strip: bool = ...
    empty_value: str | None = ...
    def __init__(
        self,
        max_length: Any | None = ...,
        min_length: Any | None = ...,
        strip: bool = ...,
        empty_value: str | None = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class IntegerField(Field):
    max_value: Any | None
    min_value: Any | None
    re_decimal: Any = ...
    def __init__(
        self,
        max_value: Any | None = ...,
        min_value: Any | None = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class FloatField(IntegerField): ...

class DecimalField(IntegerField):
    decimal_places: int | None
    max_digits: int | None
    def __init__(
        self,
        *,
        max_value: Any | None = ...,
        min_value: Any | None = ...,
        max_digits: Any | None = ...,
        decimal_places: Any | None = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class BaseTemporalField(Field):
    input_formats: Any = ...
    def __init__(
        self,
        input_formats: Any | None = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...
    def strptime(self, value: Any, format: str) -> Any: ...

class DateField(BaseTemporalField): ...
class TimeField(BaseTemporalField): ...
class DateTimeField(BaseTemporalField): ...

class DurationField(Field):
    def prepare_value(self, value: timedelta | str | None) -> str | None: ...

class RegexField(CharField):
    regex: str = ...
    def __init__(
        self,
        regex: str | Pattern[str],
        max_length: Any | None = ...,
        min_length: Any | None = ...,
        strip: bool = ...,
        empty_value: str | None = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class EmailField(CharField): ...

class FileField(Field):
    allow_empty_file: bool = ...
    def __init__(
        self,
        max_length: Any | None = ...,
        allow_empty_file: bool = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...
    def clean(self, data: Any, initial: Any | None = ...) -> Any: ...

class ImageField(FileField): ...
class URLField(CharField): ...
class BooleanField(Field): ...
class NullBooleanField(BooleanField): ...

class CallableChoiceIterator:
    choices_func: Callable[..., Any] = ...
    def __init__(self, choices_func: Callable[..., Any]) -> None: ...
    def __iter__(self) -> None: ...

class ChoiceField(Field):
    def __init__(
        self,
        choices: _FieldChoices | Callable[[], _FieldChoices] = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...
    def valid_value(self, value: str) -> bool: ...

class TypedChoiceField(ChoiceField):
    coerce: Callable[..., Any] | type[Any] = ...
    empty_value: str | None = ...
    def __init__(
        self,
        coerce: Any = ...,
        empty_value: str | None = ...,
        choices: Any = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class MultipleChoiceField(ChoiceField): ...

class TypedMultipleChoiceField(MultipleChoiceField):
    coerce: Callable[..., Any] | type[float] = ...
    empty_value: list[Any] | None = ...
    def __init__(
        self,
        coerce: Any = ...,
        empty_value: str | None = ...,
        choices: Any = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class ComboField(Field):
    fields: Any = ...
    def __init__(
        self,
        fields: Sequence[Field],
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class MultiValueField(Field):
    require_all_fields: bool = ...
    fields: Any = ...
    def __init__(
        self,
        fields: Sequence[Field],
        require_all_fields: bool = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...
    def compress(self, data_list: Any) -> Any: ...

class FilePathField(ChoiceField):
    allow_files: bool
    allow_folders: bool
    match: str | None
    path: str
    recursive: bool
    match_re: Any = ...
    def __init__(
        self,
        path: str,
        match: Any | None = ...,
        recursive: bool = ...,
        allow_files: bool = ...,
        allow_folders: bool = ...,
        choices: Any = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class SplitDateTimeField(MultiValueField):
    def __init__(
        self,
        input_date_formats: Any | None = ...,
        input_time_formats: Any | None = ...,
        fields: Sequence[Field] = ...,
        require_all_fields: bool = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...
    def compress(self, data_list: list[datetime | None]) -> datetime | None: ...

class GenericIPAddressField(CharField):
    unpack_ipv4: bool = ...
    def __init__(
        self,
        protocol: str = ...,
        unpack_ipv4: bool = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class SlugField(CharField):
    allow_unicode: bool = ...
    def __init__(
        self,
        allow_unicode: bool = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: Any | None = ...,
        initial: Any | None = ...,
        help_text: str = ...,
        error_messages: Any | None = ...,
        show_hidden_initial: bool = ...,
        validators: Sequence[Any] = ...,
        localize: bool = ...,
        disabled: bool = ...,
        label_suffix: Any | None = ...,
    ) -> None: ...

class UUIDField(CharField): ...
class InvalidJSONInput(str): ...
class JSONString(str): ...

class JSONField(CharField):
    default_error_messages: Any = ...
    widget: Any = ...
    encoder: Any = ...
    decoder: Any = ...
    def __init__(
        self, encoder: Any | None = ..., decoder: Any | None = ..., **kwargs: Any
    ) -> None: ...
    def to_python(self, value: Any) -> Any: ...
    def bound_data(self, data: Any, initial: Any) -> Any: ...
    def prepare_value(self, value: Any) -> Any: ...
    def has_changed(self, initial: Any, data: Any) -> Any: ...
