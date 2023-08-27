from collections.abc import Sequence
from typing import Any

from django.db.models import Func, Index
from django.db.models.query_utils import Q

class PostgresIndex(Index): ...

class BrinIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        autosummarize: bool | None = ...,
        pages_per_range: int | None = ...,
        fields: Sequence[str] = ...,
        name: str | None = ...,
        db_tablespace: str | None = ...,
        opclasses: Sequence[str] = ...,
        condition: Q | None = ...
    ) -> None: ...

class BTreeIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        fillfactor: int | None = ...,
        fields: Sequence[str] = ...,
        name: str | None = ...,
        db_tablespace: str | None = ...,
        opclasses: Sequence[str] = ...,
        condition: Q | None = ...
    ) -> None: ...

class GinIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        fastupdate: bool | None = ...,
        gin_pending_list_limit: int | None = ...,
        fields: Sequence[str] = ...,
        name: str | None = ...,
        db_tablespace: str | None = ...,
        opclasses: Sequence[str] = ...,
        condition: Q | None = ...
    ) -> None: ...

class GistIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        buffering: bool | None = ...,
        fillfactor: int | None = ...,
        fields: Sequence[str] = ...,
        name: str | None = ...,
        db_tablespace: str | None = ...,
        opclasses: Sequence[str] = ...,
        condition: Q | None = ...
    ) -> None: ...

class HashIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        fillfactor: int | None = ...,
        fields: Sequence[str] = ...,
        name: str | None = ...,
        db_tablespace: str | None = ...,
        opclasses: Sequence[str] = ...,
        condition: Q | None = ...
    ) -> None: ...

class SpGistIndex(PostgresIndex):
    def __init__(
        self,
        *expressions: Any,
        fillfactor: int | None = ...,
        fields: Sequence[str] = ...,
        name: str | None = ...,
        db_tablespace: str | None = ...,
        opclasses: Sequence[str] = ...,
        condition: Q | None = ...
    ) -> None: ...

class OpClass(Func):
    template: str = ...
    def __init__(
        self,
        expression: Any,
        name: str,
    ) -> None: ...
