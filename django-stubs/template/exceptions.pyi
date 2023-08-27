from typing import Optional, Union

from django.template.backends.base import BaseEngine
from django.template.base import Origin

class TemplateDoesNotExist(Exception):
    backend: Optional[BaseEngine] = ...
    tried: list[tuple[Origin, str]] = ...
    chain: list[TemplateDoesNotExist] = ...
    def __init__(
        self,
        msg: Union[Origin, str],
        tried: Optional[list[tuple[Origin, str]]] = ...,
        backend: Optional[BaseEngine] = ...,
        chain: Optional[list[TemplateDoesNotExist]] = ...,
    ) -> None: ...

class TemplateSyntaxError(Exception): ...
