from collections.abc import Sequence
from enum import Enum
from typing import Any, cast, overload
from typing_extensions import Self, deprecated

from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.models.base import Model
from django.db.models.expressions import BaseExpression, Combinable
from django.db.models.query_utils import Q
from typing_extensions import Self

class Deferrable(Enum):
    DEFERRED = cast(str, ...)
    IMMEDIATE = cast(str, ...)

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
    check: Q | BaseExpression
    condition: Q | BaseExpression

    @overload
    @deprecated(
        "check keyword argument is deprecated in favor of condition and will be removed in Django 6.0"
    )
    def __init__(
        self,
        *,
        name: str,
        condition: None = None,
        check: Q | BaseExpression,
        violation_error_code: str | None = None,
        violation_error_message: str | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        name: str,
        condition: Q | BaseExpression,
        check: None = None,
        violation_error_code: str | None = None,
        violation_error_message: str | None = None,
    ) -> None: ...

class UniqueConstraint(BaseConstraint):
    expressions: Sequence[BaseExpression | Combinable]
    fields: Sequence[str]
    condition: Q | None
    deferrable: Deferrable | None
    nulls_distinct: bool | None

    @overload
    def __init__(
        self,
        *expressions: str | BaseExpression | Combinable,
        fields: None = None,
        name: str | None = None,
        condition: Q | None = None,
        deferrable: Deferrable | None = None,
        include: Sequence[str] | None = None,
        opclasses: Sequence[Any] = (),
        nulls_distinct: bool | None = None,
        violation_error_code: str | None = None,
        violation_error_message: str | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        fields: Sequence[str],
        name: str | None = None,
        condition: Q | None = None,
        deferrable: Deferrable | None = None,
        include: Sequence[str] | None = None,
        opclasses: Sequence[Any] = (),
        nulls_distinct: bool | None = None,
        violation_error_code: str | None = None,
        violation_error_message: str | None = None,
    ) -> None: ...
