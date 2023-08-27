from collections.abc import Callable, Sequence
from typing import Any, Optional, Union

from django.apps.config import AppConfig
from django.core.checks.messages import CheckMessage, Error, Warning
from django.urls.resolvers import URLPattern, URLResolver

def check_url_config(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[CheckMessage]: ...
def check_resolver(
    resolver: Union[tuple[str, Callable[..., Any]], URLPattern, URLResolver]
) -> list[CheckMessage]: ...
def check_url_namespaces_unique(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[Warning]: ...
def get_warning_for_invalid_pattern(pattern: Any) -> list[Error]: ...
def check_url_settings(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[Error]: ...
def E006(name: str) -> Error: ...
