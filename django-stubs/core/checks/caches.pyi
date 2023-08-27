from collections.abc import Sequence
from typing import Any

from django.apps.config import AppConfig
from django.core.checks.messages import Error

E001: Any

def check_default_cache_is_configured(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> list[Error]: ...
