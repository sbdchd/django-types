from collections.abc import Iterable
from typing import Any, ClassVar, TypeVar
from typing_extensions import Self

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone as timezone

ADDITION: int
CHANGE: int
DELETION: int
ACTION_FLAG_CHOICES: list[tuple[int, str]]

_LogEntryT = TypeVar("_LogEntryT", bound=LogEntry)

class LogEntryManager(models.Manager[_LogEntryT]):
    use_in_migrations: bool
    # Deprecated in favor of log_actions
    def log_action(
        self,
        user_id: int,
        content_type_id: int,
        object_id: Any,
        object_repr: str,
        action_flag: int,
        change_message: str | list[Any] = ...,
    ) -> _LogEntryT: ...
    def log_actions(
        self,
        user_id: int,
        queryset: Iterable[models.Model],
        action_flag: int,
        change_message: str | list[Any] = ...,
        *,
        single_object: bool = ...,
    ) -> _LogEntryT | list[_LogEntryT]: ...

class LogEntry(models.Model):
    action_time = models.DateTimeField()
    user = models.ForeignKey[User]
    content_type = models.ForeignKey[ContentType]
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField()
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField(blank=True)

    objects: ClassVar[LogEntryManager[Self]]  # type: ignore[assignment]

    def is_addition(self) -> bool: ...
    def is_change(self) -> bool: ...
    def is_deletion(self) -> bool: ...
    def get_change_message(self) -> str: ...
    def get_edited_object(self) -> models.Model: ...
    def get_admin_url(self) -> str | None: ...
