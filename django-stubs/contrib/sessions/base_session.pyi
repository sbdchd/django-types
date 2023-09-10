from datetime import datetime
from typing import ClassVar, TypeVar
from typing_extensions import Self

from django.contrib.sessions.backends.base import SessionBase
from django.db import models

_SessionT = TypeVar("_SessionT", bound=AbstractBaseSession)

class BaseSessionManager(models.Manager[_SessionT]):
    def encode(self, session_dict: dict[str, int]) -> str: ...
    def save(
        self, session_key: str, session_dict: dict[str, int], expire_date: datetime
    ) -> _SessionT: ...

class AbstractBaseSession(models.Model):
    objects: ClassVar[BaseSessionManager[Self]]  # type: ignore[assignment]

    session_key: models.CharField[str]
    session_data: models.TextField[str]
    expire_date: models.DateTimeField[datetime]

    @classmethod
    def get_session_store_class(cls) -> type[SessionBase] | None: ...
    def get_decoded(self) -> dict[str, int]: ...
