from .base import run_pyright


def test_client_generic_returns_a_response() -> None:
    """Client.generic returns a response, like every other verb on Client."""
    results = run_pyright(
        """\
from django.test import Client

client = Client()
response = client.generic("PATCH", "/x/", data=b"{}", content_type="application/json")
reveal_type(response.status_code)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_url_patterns_is_heterogeneous() -> None:
    """A URL-introspection helper walks the resolver tree to enumerate routes."""
    results = run_pyright(
        """\
from django.urls import get_resolver
from django.urls.resolvers import URLResolver

for entry in get_resolver().url_patterns:
    if isinstance(entry, URLResolver):
        reveal_type(entry.namespace)
    else:
        reveal_type(entry.name)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_streaming_response_accepts_str_chunks() -> None:
    """A view streams rendered text - SSE, CSV, NDJSON - a chunk at a time."""
    results = run_pyright(
        """\
from django.http import StreamingHttpResponse

StreamingHttpResponse(iter(["a", "b"]))
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_session_payload_is_heterogeneous() -> None:
    """One decoded session holds several unrelated value types at once."""
    results = run_pyright(
        """\
from django.contrib.sessions.base_session import AbstractBaseSession

def read(session: AbstractBaseSession) -> tuple[str, int, list[dict[str, int]]]:
    data = session.get_decoded()
    user_id: str = data["_auth_user_id"]
    expiry: int = data["_session_expiry"]
    cart: list[dict[str, int]] = data["myapp_cart"]
    return user_id, expiry, cart
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_refresh_from_db_takes_any_iterable() -> None:
    """A caller refreshes a named subset of fields, passing a tuple."""
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    pass

Foo().refresh_from_db(fields=("a", "b"))
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_non_interactive_questioner_verbosity_and_log() -> None:
    """A migration-graph check drives the autodetector and wants its reasons."""
    results = run_pyright(
        """\
from django.db.migrations.questioner import NonInteractiveMigrationQuestioner

def _eprint(message: str) -> None: ...

questioner = NonInteractiveMigrationQuestioner(
    specified_apps=set(), dry_run=True, verbosity=1, log=_eprint
)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_get_query_string_takes_values_to_encode() -> None:
    """ChangeList.get_query_string carries real values, not a dict[str, None]."""
    results = run_pyright(
        """\
from django.contrib.admin.views.main import ChangeList

def f(cl: ChangeList) -> str:
    return cl.get_query_string({"p": "2", "o": "-1"}, remove=["q"])
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_sql_flush_is_keyword_only_and_returns_statements() -> None:
    """sql_flush takes reset_sequences/allow_cascade by keyword and returns list[str]."""
    results = run_pyright(
        """\
from django.core.management.color import no_style
from django.db.backends.base.operations import BaseDatabaseOperations

def f(ops: BaseDatabaseOperations) -> list[str]:
    return ops.sql_flush(no_style(), ["app_thing"], reset_sequences=True, allow_cascade=False)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_migration_loader_takes_replace_migrations() -> None:
    """MigrationLoader accepts replace_migrations, as it has since Django 3.0."""
    results = run_pyright(
        """\
from django.db import connection
from django.db.migrations.loader import MigrationLoader

loader = MigrationLoader(connection, replace_migrations=False)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_client_query_params_is_a_mapping() -> None:
    """query_params is a mapping Django urlencodes, on every verb and on generic()."""
    results = run_pyright(
        """\
from django.test.client import AsyncClient, Client

def f(c: Client) -> int:
    return c.get("/", query_params={"q": "x", "page": 2}).status_code

async def g(c: AsyncClient) -> int:
    return (await c.generic("PATCH", "/", query_params={"q": "x"})).status_code
"""
    )
    assert [r for r in results if r.type == "error"] == []
