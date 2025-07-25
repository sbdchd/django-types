import enum
from collections.abc import Sequence
from typing import Any
from typing_extensions import Self

from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import ProjectState
from django.db.models import Model

class OperationCategory(str, enum.Enum):
    ADDITION = "+"
    REMOVAL = "-"
    ALTERATION = "~"
    PYTHON = "p"
    SQL = "s"
    MIXED = "?"

class Operation:
    reversible: bool
    reduces_to_sql: bool
    atomic: bool
    elidable: bool
    serialization_expand_args: list[Any]
    category: OperationCategory | None
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...
    def deconstruct(self) -> tuple[str, Sequence[Any], dict[str, Any]]: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(
        self,
        app_label: str,
        schema_editor: BaseDatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None: ...
    def database_backwards(
        self,
        app_label: str,
        schema_editor: BaseDatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None: ...
    def describe(self) -> str: ...
    def references_model(self, name: str, app_label: str) -> bool: ...
    def references_field(self, model_name: str, name: str, app_label: str) -> bool: ...
    def allow_migrate_model(
        self, connection_alias: str, model: type[Model]
    ) -> bool | None: ...
    def reduce(
        self, operation: Operation, app_label: str
    ) -> list[Operation] | bool: ...
