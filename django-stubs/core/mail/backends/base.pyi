import types
from collections.abc import Iterable
from typing import Any
from typing_extensions import Self

from django.core.mail.message import EmailMessage

class BaseEmailBackend:
    fail_silently: bool
    def __init__(self, fail_silently: bool = ..., **kwargs: Any) -> None: ...
    def open(self) -> bool | None: ...
    def close(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        traceback: types.TracebackType,
    ) -> None: ...
    def send_messages(self, email_messages: Iterable[EmailMessage]) -> int: ...
