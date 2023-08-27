from collections.abc import Sequence
from typing import Any

from django.apps.config import AppConfig

from . import Error

E001: Error = ...

def check_setting_language_code(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> list[Error]: ...
