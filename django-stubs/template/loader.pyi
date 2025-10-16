from typing import Any

from django.http.request import HttpRequest
from django.template.backends.base import _BaseTemplate
from django.template.exceptions import TemplateDoesNotExist as TemplateDoesNotExist
from django.utils.safestring import SafeText

from . import engines as engines

def get_template(template_name: str, using: str | None = ...) -> _BaseTemplate: ...
def select_template(
    template_name_list: list[str] | str, using: str | None = ...
) -> _BaseTemplate: ...
def render_to_string(
    template_name: list[str] | str,
    context: dict[str, Any] | None = ...,
    request: HttpRequest | None = ...,
    using: str | None = ...,
) -> SafeText: ...
