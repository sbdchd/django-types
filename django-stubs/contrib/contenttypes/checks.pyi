from collections.abc import Sequence
from typing import Any, Optional

from django.apps.config import AppConfig

def check_generic_foreign_keys(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[Any]: ...
def check_model_name_lengths(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[Any]: ...
