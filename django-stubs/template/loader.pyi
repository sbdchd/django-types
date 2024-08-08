from typing import Any

from django.http.request import HttpRequest
from django.template.backends.base import _BaseTemplate
from django.template.exceptions import (  # noqa: F401
    TemplateDoesNotExist as TemplateDoesNotExist,
)
from django.utils.safestring import SafeText

from . import engines as engines  # noqa: F401

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
