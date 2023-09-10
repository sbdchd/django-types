from typing import ClassVar, TypeVar
from typing_extensions import Self

from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.base_session import AbstractBaseSession, BaseSessionManager

_T = TypeVar("_T", bound=AbstractBaseSession)

class SessionManager(BaseSessionManager[_T]): ...

class Session(AbstractBaseSession):
    objects: ClassVar[SessionManager[Self]]  # type: ignore[assignment]

    @classmethod
    def get_session_store_class(cls) -> type[SessionStore]: ...
