from typing import Optional, Union

from django.db.backends.base.client import BaseDatabaseClient

class DatabaseClient(BaseDatabaseClient):
    executable_name: str = ...
    @classmethod
    def settings_to_cmd_args(
        cls,
        settings_dict: dict[str, Optional[Union[dict[str, dict[str, str]], int, str]]],
    ) -> list[str]: ...
    def runshell(self) -> None: ...
