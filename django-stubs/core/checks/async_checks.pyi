from collections.abc import Sequence
from typing import Any, Optional

from django.apps.config import AppConfig

E001: Any

def check_async_unsafe(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> Any: ...
