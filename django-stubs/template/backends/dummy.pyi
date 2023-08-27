import string
from typing import Any, Optional, Union

from django.http.request import HttpRequest

from .base import BaseEngine

class TemplateStrings(BaseEngine):
    template_dirs: tuple[str]
    def __init__(
        self, params: dict[str, Union[dict[Any, Any], list[Any], bool, str]]
    ) -> None: ...

class Template(string.Template):
    template: str
    def render(
        self,
        context: Optional[dict[str, str]] = ...,
        request: Optional[HttpRequest] = ...,
    ) -> str: ...
