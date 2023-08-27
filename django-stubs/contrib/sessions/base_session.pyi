from datetime import datetime
from typing import Any, ClassVar

from django.contrib.sessions.backends.base import SessionBase
from django.db import models

class BaseSessionManager(models.Manager[Any]):
    def encode(self, session_dict: dict[str, int]) -> str: ...
    def save(
        self, session_key: str, session_dict: dict[str, int], expire_date: datetime
    ) -> AbstractBaseSession: ...

class AbstractBaseSession(models.Model):
    expire_date: datetime
    session_data: str
    session_key: str
    objects: ClassVar[BaseSessionManager] = ...
    @classmethod
    def get_session_store_class(cls) -> type[SessionBase] | None: ...
    def get_decoded(self) -> dict[str, int]: ...
