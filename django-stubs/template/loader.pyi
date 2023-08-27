from typing import Any, Optional, Union

from django.http.request import HttpRequest
from django.template.exceptions import (  # noqa: F401
    TemplateDoesNotExist as TemplateDoesNotExist,
)

from . import engines as engines  # noqa: F401

def get_template(template_name: str, using: Optional[str] = ...) -> Any: ...
def select_template(
    template_name_list: Union[list[str], str], using: Optional[str] = ...
) -> Any: ...
def render_to_string(
    template_name: Union[list[str], str],
    context: Optional[dict[str, Any]] = ...,
    request: Optional[HttpRequest] = ...,
    using: Optional[str] = ...,
) -> str: ...
