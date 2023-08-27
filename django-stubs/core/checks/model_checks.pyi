from collections.abc import Sequence
from typing import Any, Optional

from django.apps.config import AppConfig
from django.core.checks.messages import Warning

def check_all_models(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[Warning]: ...
def check_lazy_references(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[Any]: ...
