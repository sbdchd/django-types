import string
from collections.abc import Mapping
from typing import Any
from typing_extensions import override

from django.http.request import HttpRequest

from .base import BaseEngine

class TemplateStrings(BaseEngine):
    @override
    def from_string(self, template_code: str) -> Template: ...
    @override
    def get_template(self, template_name: str) -> Template: ...

class Template(string.Template):
    def render(
        self,
        context: Mapping[str, Any] | None = ...,
        request: HttpRequest | None = ...,
    ) -> str: ...
