from collections.abc import Sequence
from typing import Any

from django.apps.config import AppConfig
from django.core.checks.messages import Warning

W003: Any
W016: Any

def check_csrf_middleware(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> list[Warning]: ...
def check_csrf_cookie_secure(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> list[Warning]: ...
