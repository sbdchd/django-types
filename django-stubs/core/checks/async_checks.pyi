from collections.abc import Sequence
from typing import Any

from django.apps.config import AppConfig

E001: Any

def check_async_unsafe(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> Any: ...
