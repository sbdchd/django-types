from collections.abc import Sequence
from typing import Any, Optional

from django.apps.config import AppConfig
from django.core.checks.messages import Error

def check_finders(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[Error]: ...
