from collections.abc import Callable
from typing import Any

from django.db import DefaultConnectionProxy
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.migrations.migration import Migration

from .loader import MigrationLoader
from .recorder import MigrationRecorder
from .state import ProjectState

class MigrationExecutor:
    connection: Any = ...
    loader: MigrationLoader = ...
    recorder: MigrationRecorder = ...
    progress_callback: Callable[..., Any] = ...
    def __init__(
        self,
        connection: DefaultConnectionProxy | BaseDatabaseWrapper | None,
        progress_callback: Callable[..., Any] | None = ...,
    ) -> None: ...
    def migration_plan(
        self,
        targets: list[tuple[str, str | None]] | set[tuple[str, str]],
        clean_start: bool = ...,
    ) -> list[tuple[Migration, bool]]: ...
    def migrate(
        self,
        targets: list[tuple[str, str | None]] | None,
        plan: list[tuple[Migration, bool]] | None = ...,
        state: ProjectState | None = ...,
        fake: bool = ...,
        fake_initial: bool = ...,
    ) -> ProjectState: ...
    def collect_sql(self, plan: list[tuple[Migration, bool]]) -> list[str]: ...
    def apply_migration(
        self,
        state: ProjectState,
        migration: Migration,
        fake: bool = ...,
        fake_initial: bool = ...,
    ) -> ProjectState: ...
    def unapply_migration(
        self, state: ProjectState, migration: Migration, fake: bool = ...
    ) -> ProjectState: ...
    def check_replacements(self) -> None: ...
    def detect_soft_applied(
        self, project_state: ProjectState | None, migration: Migration
    ) -> tuple[bool, ProjectState]: ...
