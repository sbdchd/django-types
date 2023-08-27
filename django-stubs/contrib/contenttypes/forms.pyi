from typing import Any

from django.forms.models import BaseModelFormSet

class BaseGenericInlineFormSet(BaseModelFormSet):
    instance: Any = ...
    rel_name: Any = ...
    save_as_new: Any = ...
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

def generic_inlineformset_factory(
    model: Any,
    form: Any = ...,
    formset: Any = ...,
    ct_field: str = ...,
    fk_field: str = ...,
    fields: Any | None = ...,
    exclude: Any | None = ...,
    extra: int = ...,
    can_order: bool = ...,
    can_delete: bool = ...,
    max_num: Any | None = ...,
    formfield_callback: Any | None = ...,
    validate_max: bool = ...,
    for_concrete_model: bool = ...,
    min_num: Any | None = ...,
    validate_min: bool = ...,
) -> Any: ...
