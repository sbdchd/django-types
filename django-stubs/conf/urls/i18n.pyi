from collections.abc import Callable
from typing import Any

from django.urls.resolvers import URLPattern

def i18n_patterns(
    *urls: Any, prefix_default_language: bool = ...
) -> list[list[URLPattern]]: ...
def is_language_prefix_patterns_used(urlconf: str) -> tuple[bool, bool]: ...

urlpatterns: list[Callable[..., Any]]
