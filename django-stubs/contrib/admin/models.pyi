import datetime as dt
from typing import Any, ClassVar, TypeVar
from typing_extensions import Self
from uuid import UUID

from django.contrib.contenttypes.models import ContentType
from django.db import models

ADDITION: int
CHANGE: int
DELETION: int
ACTION_FLAG_CHOICES: list[tuple[int, str]]

_LogEntryT = TypeVar("_LogEntryT", bound=LogEntry)

class LogEntryManager(models.Manager[_LogEntryT]):
    def log_action(
        self,
        user_id: int,
        content_type_id: int,
        object_id: int | str | UUID,
        object_repr: str,
        action_flag: int,
        change_message: str | list[Any] = ...,
    ) -> _LogEntryT: ...

class LogEntry(models.Model):
    objects: ClassVar[LogEntryManager[Self]]  # type: ignore[assignment]

    action_time: models.DateTimeField[dt.datetime]
    user: models.ForeignKey[Any]
    content_type: models.ForeignKey[ContentType | None]
    object_id: models.TextField[str | None]
    object_repr: models.CharField[str]
    action_flag: models.PositiveSmallIntegerField[int]
    change_message: models.TextField[str]

    def is_addition(self) -> bool: ...
    def is_change(self) -> bool: ...
    def is_deletion(self) -> bool: ...
    def get_change_message(self) -> str: ...
    def get_edited_object(self) -> models.Model: ...
    def get_admin_url(self) -> str | None: ...
