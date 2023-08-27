from django.db.backends.base.client import BaseDatabaseClient

class DatabaseClient(BaseDatabaseClient):
    executable_name: str = ...
    @classmethod
    def settings_to_cmd_args(
        cls,
        settings_dict: dict[str, dict[str, dict[str, str]] | int | str | None],
    ) -> list[str]: ...
    def runshell(self) -> None: ...
