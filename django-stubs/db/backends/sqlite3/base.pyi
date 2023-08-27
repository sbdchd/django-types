from collections.abc import Callable
from sqlite3 import dbapi2 as Database
from typing import Any

from django.db.backends.base.base import BaseDatabaseWrapper

def decoder(conv_func: Callable[..., Any]) -> Callable[..., Any]: ...

class DatabaseWrapper(BaseDatabaseWrapper): ...

FORMAT_QMARK_REGEX: Any

class SQLiteCursorWrapper(Database.Cursor): ...

def check_sqlite_version() -> None: ...
