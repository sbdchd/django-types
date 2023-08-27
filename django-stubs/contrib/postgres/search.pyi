from collections.abc import Iterable
from typing import Any
from typing_extensions import Self

from django.db.models import Field
from django.db.models.expressions import (
    Combinable,
    CombinedExpression,
    Func,
    Value,
    _OutputField,
)
from django.db.models.fields import (
    _ErrorMessagesToOverride,
    _FieldChoices,
    _ValidatorCallable,
)
from django.db.models.lookups import Lookup

_Expression = str | Combinable | SearchQueryCombinable

class SearchVectorExact(Lookup[Any]): ...

class SearchVectorField(Field[Any, Any]):
    def __init__(
        self,
        verbose_name: str | bytes | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: _FieldChoices | None = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> None: ...

class SearchQueryField(Field[Any, Any]):
    def __init__(
        self,
        verbose_name: str | bytes | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: _FieldChoices | None = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> None: ...

class SearchVectorCombinable:
    ADD: str = ...

class SearchVector(SearchVectorCombinable, Func):
    config: Any | None = ...
    def __init__(self, *expressions: _Expression, **extra: Any) -> None: ...

class CombinedSearchVector(SearchVectorCombinable, CombinedExpression):
    def __init__(
        self,
        lhs: Any,
        connector: Any,
        rhs: Any,
        config: _Expression | None = ...,
        output_field: _OutputField | None = ...,
    ) -> None: ...

class SearchQueryCombinable:
    BITAND: str = ...
    BITOR: str = ...
    def __or__(self, other: SearchQueryCombinable) -> Self: ...
    def __ror__(self, other: SearchQueryCombinable) -> Self: ...
    def __and__(self, other: SearchQueryCombinable) -> Self: ...
    def __rand__(self, other: SearchQueryCombinable) -> Self: ...

class SearchQuery(SearchQueryCombinable, Value):  # type: ignore
    SEARCH_TYPES: dict[str, str] = ...
    def __init__(
        self,
        value: str,
        output_field: _OutputField | None = ...,
        *,
        config: _Expression | None = ...,
        invert: bool = ...,
        search_type: str = ...
    ) -> None: ...
    def __invert__(self) -> Self: ...

class CombinedSearchQuery(SearchQueryCombinable, CombinedExpression):  # type: ignore
    def __init__(
        self,
        lhs: Any,
        connector: Any,
        rhs: Any,
        config: _Expression | None = ...,
        output_field: _OutputField | None = ...,
    ) -> None: ...

class SearchRank(Func):
    def __init__(
        self,
        vector: SearchVector | _Expression,
        query: SearchQuery | _Expression,
        **extra: Any
    ) -> None: ...

class TrigramBase(Func):
    def __init__(self, expression: _Expression, string: str, **extra: Any) -> None: ...

class TrigramSimilarity(TrigramBase): ...
class TrigramDistance(TrigramBase): ...
