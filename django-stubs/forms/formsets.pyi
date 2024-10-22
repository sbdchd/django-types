from collections.abc import Iterator
from typing import Any, Generic, TypeVar

from django.forms import BaseForm, Form
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorDict, ErrorList, RenderableFormMixin
from django.forms.widgets import CheckboxInput, Media, NumberInput, Widget

TOTAL_FORM_COUNT: str
INITIAL_FORM_COUNT: str
MIN_NUM_FORM_COUNT: str
MAX_NUM_FORM_COUNT: str
ORDERING_FIELD_NAME: str
DELETION_FIELD_NAME: str

DEFAULT_MIN_NUM: int
DEFAULT_MAX_NUM: int

_BaseFormT = TypeVar("_BaseFormT", bound=BaseForm)

class ManagementForm(Form): ...

class BaseFormSet(Generic[_BaseFormT], RenderableFormMixin):
    deletion_widget: type[CheckboxInput]
    ordering_widget: type[NumberInput]
    default_error_messages: dict[str, str]
    template_name_div: str
    template_name_p: str
    template_name_table: str
    template_name_ul: str

    is_bound: bool
    prefix: str
    auto_id: str
    data: dict[str, Any]
    files: dict[str, Any]
    initial: dict[str, Any] | None
    form_kwargs: dict[str, Any]
    error_class: type[ErrorList]
    error_messages: dict[str, Any]

    def __init__(
        self,
        data: dict[str, Any] | None = ...,
        files: dict[str, Any] | None = ...,
        auto_id: str = ...,
        prefix: str | None = ...,
        initial: dict[str, Any] | None = ...,
        error_class: type[ErrorList] = ...,
        form_kwargs: dict[str, Any] | None = ...,
        error_messages: dict[str, Any] | None = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[_BaseFormT]: ...
    def __getitem__(self, index: int) -> _BaseFormT: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    @property
    def management_form(self) -> ManagementForm: ...
    def total_form_count(self) -> int: ...
    def initial_form_count(self) -> int: ...
    @property
    def forms(self) -> list[_BaseFormT]: ...
    def get_form_kwargs(self, index: int) -> dict[str, Any]: ...
    @property
    def initial_forms(self) -> list[_BaseFormT]: ...
    @property
    def extra_forms(self) -> list[_BaseFormT]: ...
    @property
    def empty_form(self) -> _BaseFormT: ...
    @property
    def cleaned_data(self) -> list[dict[str, Any]]: ...
    @property
    def deleted_forms(self) -> list[_BaseFormT]: ...
    @property
    def ordered_forms(self) -> list[_BaseFormT]: ...
    @classmethod
    def get_default_prefix(cls) -> str: ...
    @classmethod
    def get_deletion_widget(cls) -> type[Widget]: ...
    @classmethod
    def get_ordering_widget(cls) -> type[Widget]: ...
    def non_form_errors(self) -> ErrorList: ...
    @property
    def errors(self) -> list[ErrorDict]: ...
    def total_error_count(self) -> int: ...
    def is_valid(self) -> bool: ...
    def full_clean(self) -> None: ...
    def clean(self) -> None: ...
    def has_changed(self) -> bool: ...
    def add_fields(self, form: _BaseFormT, index: int) -> None: ...
    def add_prefix(self, index: int) -> str: ...
    def is_multipart(self) -> bool: ...
    @property
    def media(self) -> Media: ...
    def get_context(self) -> dict[str, Any]: ...

# Dynamic class produced by formset_factory
class _FormSet(BaseFormSet[_BaseFormT]):
    form: type[_BaseFormT]
    extra: int
    can_order: bool
    can_delete: bool
    can_delete_extra: bool
    min_num: int
    max_num: int
    absolute_max: int
    validate_min: bool
    validate_max: bool
    renderer: BaseRenderer

def formset_factory(
    form: _BaseFormT,
    formset: type[BaseFormSet[_BaseFormT]] = ...,
    extra: int = ...,
    can_order: bool = ...,
    can_delete: bool = ...,
    max_num: int | None = ...,
    validate_max: bool = ...,
    min_num: int | None = ...,
    validate_min: bool = ...,
    absolute_max: int | None = ...,
    can_delete_extra: bool = ...,
    renderer: BaseRenderer | None = ...,
) -> type[_FormSet[_BaseFormT]]: ...
def all_valid(formsets: Iterator[BaseFormSet[Any]]) -> bool: ...
