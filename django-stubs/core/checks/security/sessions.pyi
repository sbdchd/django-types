from collections.abc import Sequence
from typing import Any

from django.apps.config import AppConfig
from django.core.checks.messages import Warning

def add_session_cookie_message(message: Any) -> Any: ...

W010: Any
W011: Any
W012: Any

def add_httponly_message(message: Any) -> Any: ...

W013: Any
W014: Any
W015: Any

def check_session_cookie_secure(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> list[Warning]: ...
def check_session_cookie_httponly(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> list[Warning]: ...
