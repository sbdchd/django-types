from collections.abc import Sequence
from enum import Enum
from typing import Any
from typing_extensions import Self

from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.models.base import Model
from django.db.models.expressions import BaseExpression, Combinable
from django.db.models.query_utils import Q

class Deferrable(Enum):
    DEFERRED: str
    IMMEDIATE: str

class BaseConstraint:
    name: str
    def __init__(
        self,
        *args: BaseExpression | Combinable | str,
        name: str | None = ...,
        violation_error_message: str | None = ...,
    ) -> None: ...
    def constraint_sql(
        self,
        model: type[Model] | None,
        schema_editor: BaseDatabaseSchemaEditor | None,
    ) -> str: ...
    def create_sql(
        self,
        model: type[Model] | None,
        schema_editor: BaseDatabaseSchemaEditor | None,
    ) -> str: ...
    def remove_sql(
        self,
        model: type[Model] | None,
        schema_editor: BaseDatabaseSchemaEditor | None,
    ) -> str: ...
    def deconstruct(self) -> Any: ...
    def clone(self) -> Self: ...

class CheckConstraint(BaseConstraint):
    check: Q
    def __init__(
        self,
        *,
        check: Q,
        name: str,
        violation_error_message: str | None = ...,
    ) -> None: ...

class UniqueConstraint(BaseConstraint):
    fields: tuple[str]
    condition: Q | None
    def __init__(
        self,
        *expressions: BaseExpression | Combinable | str,
        fields: Sequence[str] = ...,
        name: str | None = ...,
        condition: Q | None = ...,
        deferrable: Deferrable | None = ...,
        include: str | Sequence[str] | None = ...,
        opclasses: Sequence[str] = ...,
        violation_error_message: str | None = ...,
    ) -> None: ...
