from collections import OrderedDict
from collections.abc import Iterator, Mapping, Sequence
from re import Pattern
from typing import Any, NamedTuple, overload
from typing_extensions import Literal, Protocol

from psycopg2._psycopg import ReplicationConnection as _replicationConnection
from psycopg2._psycopg import ReplicationCursor as _replicationCursor
from psycopg2._range import DateRange as DateRange
from psycopg2._range import DateTimeTZRange as DateTimeTZRange
from psycopg2._range import NumericRange as NumericRange
from psycopg2._range import Range as Range
from psycopg2.extensions import _SQLType
from psycopg2.extensions import connection as _connection
from psycopg2.extensions import cursor as _cursor

class DictCursorBase(_cursor):
    _query_executed: bool
    _prefetch: bool
    row_factory: Any
    def __init__(self, *args: Any, row_factory: Any | None, **kwargs: Any) -> None: ...
    def fetchone(self) -> tuple[Any, ...] | None: ...
    def fetchmany(self, size: int | None = ...) -> list[tuple[Any, ...]]: ...
    def fetchall(self) -> list[tuple[Any, ...]]: ...
    def __iter__(self) -> Iterator[tuple[Any, ...]]: ...

class DictConnection(_connection):
    def cursor(
        self, *args: Any, cursor_factory: DictCursorBase | None = ..., **kwargs: Any
    ) -> _cursor: ...

class DictCursor(DictCursorBase):
    index: OrderedDict[str, int]
    _query_executed: bool
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def execute(
        self,
        query: str,
        vars: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...
    def callproc(
        self,
        procname: str,
        parameters: Sequence[_SQLType] | Mapping[str, _SQLType] = ...,
    ) -> None: ...

class DictRow(list[Any]):
    _index: OrderedDict[str, int]
    def __init__(self, cursor: DictCursor) -> None: ...
    def __getitem__(self, x: str | int | slice) -> Any: ...  # type: ignore [override]
    def __setitem__(self, x: str | int | slice, v: Any) -> None: ...  # type: ignore [override]
    def items(self) -> Iterator[tuple[str, Any]]: ...
    def keys(self) -> Iterator[str]: ...
    def values(self) -> Iterator[Any]: ...
    def get(self, x: str | int | slice, default: Any | None = ...) -> Any | None: ...
    def copy(self) -> OrderedDict[str, Any]: ...  # type: ignore [override]
    def __contains__(self, x: str) -> bool: ...  # type: ignore [override]
    def __getstate__(self) -> tuple[Any, OrderedDict[str, int]]: ...
    def __setstate__(self, data: tuple[Any, OrderedDict[str, int]]) -> None: ...

class RealDictConnection(_connection):
    def cursor(  # type: ignore [override]
        self, *args: Any, cursor_factory: RealDictCursor, **kwargs: Any
    ) -> _cursor: ...

class RealDictCursor(DictCursorBase):
    column_mapping: list[Any]
    _query_executed: bool
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def execute(
        self,
        query: str,
        vars: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...
    def callproc(
        self,
        procname: str,
        vars: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...

class RealDictRow(OrderedDict[Any, Any]):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...

class NamedTupleConnection(_connection):
    def cursor(self, *args: Any, **kwargs: Any) -> _cursor: ...

class NamedTupleCursor(_cursor):
    Record: NamedTuple | None = ...
    MAX_CACHE: int = ...
    def execute(
        self,
        query: str,
        vars: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...
    def executemany(
        self,
        query: str,
        vars_list: Sequence[Sequence[_SQLType] | Mapping[str, _SQLType]],
    ) -> None: ...
    def callproc(
        self,
        procname: str,
        vars: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...
    def fetchone(self) -> tuple[Any, ...] | None: ...
    def fetchmany(self, size: int = ...) -> list[tuple[Any, ...]]: ...
    def fetchall(self) -> list[tuple[Any, ...]]: ...
    def __iter__(self) -> Iterator[tuple[Any, ...]]: ...

class LoggingConnection(_connection):
    def initialize(self, logobj: Any) -> None: ...
    def filter(self, msg: Any, curs: Any) -> Any: ...
    def cursor(self, *args: Any, **kwargs: Any) -> _cursor: ...

class LoggingCursor(_cursor):
    def execute(
        self,
        query: str,
        vars: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...
    def callproc(
        self,
        procname: str,
        vars: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...

class MinTimeLoggingConnection(LoggingConnection):
    def initialize(self, logobj: Any, mintime: int = ...) -> None: ...
    def filter(self, msg: Any, curs: Any) -> str | None: ...
    def cursor(self, *args: Any, **kwargs: Any) -> _cursor: ...

class MinTimeLoggingCursor(LoggingCursor):
    timestamp: float
    def execute(
        self,
        query: str,
        vars: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...
    def callproc(
        self,
        procname: str,
        vars: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...

class LogicalReplicationConnection(_replicationConnection):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class PhysicalReplicationConnection(_replicationConnection):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class StopReplication(Exception): ...

class ReplicationCursor(_replicationCursor):
    def create_replication_slot(
        self,
        slot_name: Any,
        slot_type: Any | None = ...,
        output_plugin: Any | None = ...,
    ) -> None: ...
    def drop_replication_slot(self, slot_name: Any) -> None: ...
    def start_replication(
        self,
        slot_name: Any | None = ...,
        slot_type: Any | None = ...,
        start_lsn: int = ...,
        timeline: int = ...,
        options: Mapping[Any, Any] | None = ...,
        decode: bool = ...,
    ) -> None: ...
    def fileno(self) -> Any: ...

class UUID_adapter:
    _uuid: Any
    def __init__(self, uuid: Any) -> None: ...
    def __conform__(self, proto: Any) -> UUID_adapter | None: ...
    def getquoted(self) -> str: ...

def register_uuid(
    oids: Any | None = ..., conn_or_curs: _cursor | _connection | None = ...
) -> None: ...

class Inet:
    addr: Any
    _conn: _connection
    def __init__(self, addr: Any) -> None: ...
    def prepare(self, conn: _connection) -> None: ...
    def getquoted(self) -> bytes: ...
    def __conform__(self, proto: Any) -> Inet | None: ...

def register_inet(
    oid: int | None = ..., conn_or_curs: _connection | _cursor | None = ...
) -> Inet: ...
def wait_select(conn: _connection) -> None: ...

class HstoreAdapter:
    wrapped: Any
    conn: _connection
    def __init__(self, wrapped: Any) -> None: ...
    def prepare(self, conn: _connection) -> None: ...
    def _getquoted_9(self) -> bytes: ...
    getquoted = _getquoted_9
    @classmethod
    def parse(
        cls, s: str | None, cur: _cursor, _bsdec: Pattern[str] = ...
    ) -> dict[str, str] | None: ...
    @classmethod
    def parse_unicode(cls, s: str | None, cur: _cursor) -> dict[str, str] | None: ...
    @classmethod
    def get_oids(
        cls, conn_or_curs: _connection | _cursor
    ) -> tuple[tuple[Any, ...], tuple[Any, ...]]: ...

def register_hstore(
    conn_or_curs: _connection | _cursor,
    globally: bool = ...,
    unicode: bool = ...,
    oid: int | None = ...,
    array_oid: int | None = ...,
) -> None: ...

class CompositeCaster:
    name: str
    schema: Any | None
    oid: int
    array_oid: int | None
    attrnames: list[Any]
    attrtypes: list[Any]
    typecaster: Any
    array_typecaster: Any | None
    def __init__(
        self,
        name: str,
        oid: int,
        attrs: Any,
        array_oid: int | None = ...,
        schema: Any | None = ...,
    ) -> None: ...
    def parse(self, s: str | None, curs: Any) -> Any: ...
    def make(self, values: Any) -> Any: ...
    @classmethod
    def tokenize(cls, s: str) -> list[str | None]: ...

def register_composite(
    name: str,
    conn_or_curs: _connection | _cursor,
    globally: bool = ...,
    factory: CompositeCaster | None = ...,
) -> CompositeCaster: ...

class _CursorLike(Protocol):
    @property
    def connection(self) -> _connection: ...
    def mogrify(
        self,
        operation: str,
        parameters: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> bytes: ...
    def execute(
        self,
        sql: str,
        params: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...
    def fetchall(self) -> list[tuple[Any, ...]]: ...

def execute_batch(
    cur: _CursorLike,
    sql: str,
    argslist: Sequence[Sequence[_SQLType] | Mapping[str, _SQLType]],
    page_size: int = ...,
) -> None: ...
@overload
def execute_values(
    cur: _CursorLike,
    sql: str,
    argslist: Sequence[Sequence[_SQLType] | Mapping[str, _SQLType]],
    *,
    template: bytes | None = ...,
    page_size: int = ...,
    fetch: Literal[True],
) -> list[tuple[Any, ...]]: ...
@overload
def execute_values(
    cur: _CursorLike,
    sql: str,
    argslist: Sequence[Sequence[_SQLType] | Mapping[str, _SQLType]],
    *,
    template: bytes | None = ...,
    page_size: int = ...,
    fetch: Literal[False] = ...,
) -> None: ...
