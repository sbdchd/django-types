from collections.abc import Iterator, Mapping
from typing import Any, ClassVar

from django.core.exceptions import ValidationError as ValidationError
from django.core.files import uploadedfile
from django.forms.boundfield import BoundField
from django.forms.fields import Field
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorDict, ErrorList, RenderableFormMixin
from django.forms.widgets import Media, MediaDefiningClass
from django.utils.datastructures import MultiValueDict
from django.utils.safestring import SafeText

class DeclarativeFieldsMetaclass(MediaDefiningClass): ...

class BaseForm(RenderableFormMixin):
    default_renderer: type[BaseRenderer]
    field_order: list[str] | None
    use_required_attribute: bool
    is_bound: bool
    data: dict[str, Any]
    files: MultiValueDict[str, uploadedfile.UploadedFile]
    auto_id: bool | str
    initial: dict[str, Any]
    error_class: type[ErrorList]
    prefix: str | None
    label_suffix: str
    empty_permitted: bool
    fields: dict[str, Field]
    renderer: BaseRenderer
    cleaned_data: dict[str, Any]
    def __init__(
        self,
        data: Mapping[str, Any] | None = ...,
        files: Mapping[str, Any] | None = ...,
        auto_id: bool | str | None = ...,
        prefix: str | None = ...,
        initial: Mapping[str, Any] | None = ...,
        error_class: type[ErrorList] = ...,
        label_suffix: str | None = ...,
        empty_permitted: bool = ...,
        field_order: list[str] | None = ...,
        use_required_attribute: bool | None = ...,
        renderer: type[BaseRenderer] | None = ...,
    ) -> None: ...
    def order_fields(self, field_order: list[str] | None) -> None: ...
    def __iter__(self) -> Iterator[BoundField]: ...
    def __getitem__(self, name: str) -> BoundField: ...
    @property
    def errors(self) -> ErrorDict: ...
    def is_valid(self) -> bool: ...
    def add_prefix(self, field_name: str) -> str: ...
    def add_initial_prefix(self, field_name: str) -> str: ...
    def non_field_errors(self) -> ErrorList: ...
    def add_error(self, field: str | None, error: ValidationError | str) -> None: ...
    def has_error(self, field: str, code: str | None = ...) -> bool: ...
    def full_clean(self) -> None: ...
    def clean(self) -> dict[str, Any]: ...
    def has_changed(self) -> bool: ...
    @property
    def changed_data(self) -> list[str]: ...
    @property
    def media(self) -> Media: ...
    def is_multipart(self) -> bool: ...
    def hidden_fields(self) -> list[BoundField]: ...
    def visible_fields(self) -> list[BoundField]: ...
    def get_initial_for_field(self, field: Field, field_name: str) -> Any: ...
    def _html_output(
        self,
        normal_row: str,
        error_row: str,
        row_ender: str,
        help_text_html: str,
        errors_on_separate_row: bool,
    ) -> SafeText: ...

class Form(BaseForm, metaclass=DeclarativeFieldsMetaclass):
    base_fields: ClassVar[dict[str, Field]]
    declared_fields: ClassVar[dict[str, Field]]
