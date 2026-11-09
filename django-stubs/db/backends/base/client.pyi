from collections.abc import Mapping
from typing import Any, ClassVar

from django.db.backends.base.base import BaseDatabaseWrapper

class BaseDatabaseClient:
    executable_name: ClassVar[str | None]
    connection: BaseDatabaseWrapper
    def __init__(self, connection: BaseDatabaseWrapper) -> None: ...
    @classmethod
    def settings_to_cmd_args_env(
        cls, settings_dict: dict[str, Any], parameters: list[str]
    ) -> tuple[list[str], Mapping[str, str] | None]: ...
    def runshell(self, parameters: list[str]) -> None: ...
