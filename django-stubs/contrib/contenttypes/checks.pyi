from collections.abc import Sequence
from typing import Any

from django.apps.config import AppConfig

def check_generic_foreign_keys(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> list[Any]: ...
def check_model_name_lengths(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> list[Any]: ...
