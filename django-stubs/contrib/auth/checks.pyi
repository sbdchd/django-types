from collections.abc import Sequence
from typing import Any, Optional

from django.apps.config import AppConfig
from django.core.checks.messages import CheckMessage

def check_user_model(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[CheckMessage]: ...
def check_models_permissions(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> list[Any]: ...
