from collections.abc import Mapping
from typing import Any
from typing_extensions import override

from django.http.request import HttpRequest
from django.template.backends.base import BaseEngine, _BaseTemplate
from django.template.backends.django import Template as DjangoTemplate
from django.template.backends.jinja2 import Template as Jinja2Template
from django.utils.safestring import SafeText

def get_default_renderer() -> BaseRenderer: ...

class BaseRenderer:
    form_template_name: str
    formset_template_name: str
    def get_template(self, template_name: str) -> _BaseTemplate: ...
    def render(
        self,
        template_name: str,
        context: Mapping[str, Any],
        request: HttpRequest | None = ...,
    ) -> SafeText: ...

class EngineMixin:
    backend: BaseEngine
    def get_template(self, template_name: str) -> _BaseTemplate: ...
    @property
    def engine(self) -> BaseEngine: ...

class DjangoTemplates(EngineMixin, BaseRenderer):
    @override
    def get_template(self, template_name: str) -> DjangoTemplate: ...

class Jinja2(EngineMixin, BaseRenderer):
    @override
    def get_template(self, template_name: str) -> Jinja2Template: ...

class DjangoDivFormRenderer(DjangoTemplates): ...
class Jinja2DivFormRenderer(Jinja2): ...
class TemplatesSetting(BaseRenderer): ...
