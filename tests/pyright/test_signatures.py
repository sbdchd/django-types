from .base import Result, run_pyright


def test_client_generic_returns_a_response() -> None:
    """A test sends a verb the Client has no named helper for - PATCH, or a
    content-type negotiation case - via client.generic().

    Client overrides get/post/head/options/put/patch/delete/trace to return a
    response, but not generic(), so it inherited RequestFactory.generic() and the
    result typed as a WSGIRequest. Every .status_code and .content on it was then
    an unknown attribute of a request object.
    """
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
    """A URL-introspection helper walks the resolver tree to enumerate routes.

    include() nests a URLResolver inside url_patterns, so walking it means
    branching on URLResolver vs URLPattern. The stub declared the list as
    list[tuple[str, Callable]], which matches neither.
    """
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


def test_multivaluedict_getitem_returns_the_value() -> None:
    """A view reads a single query parameter and converts it.

    QueryDict[...] returns the last value for the key; getlist() is the API that
    returns every value. The stub returned the union of both, so int(params["pk"])
    was rejected on the list arm that subscripting never produces.
    """
    results = run_pyright(
        """\
from django.http import QueryDict

def read(params: QueryDict) -> int:
    return int(params["pk"])
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_streaming_response_accepts_str_chunks() -> None:
    """A view streams rendered text - SSE, CSV, NDJSON - a chunk at a time.

    StreamingHttpResponse encodes str chunks itself, so yielding str is ordinary
    usage, but the stub accepted only bytes.
    """
    results = run_pyright(
        """\
from django.http import StreamingHttpResponse

StreamingHttpResponse(iter(["a", "b"]))
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_session_payload_is_heterogeneous() -> None:
    """One decoded session holds several unrelated value types at once.

    Django itself writes _auth_user_id as a str (pk.value_to_string),
    _session_expiry as an int and _auth_user_backend as a str, and any installed
    app adds keys of its own. So no single value type fits - the stub said
    dict[str, int], wrong for two of the three keys Django writes - and there is
    no union to close over, because the key space is open. This test is what a
    narrower annotation would have to satisfy.
    """
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
    """A caller refreshes a named subset of fields, passing a tuple.

    The field names are a fixed set at the call site, so a tuple is the natural
    literal; the stub required list[str] specifically.
    """
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    pass

Foo().refresh_from_db(fields=("a", "b"))
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_callable_field_choices() -> None:
    """A choices callable keeps a new enum member from needing a migration.

    Django serializes the reference rather than the values, so a callable is the
    documented way to avoid a migration per member. `Field.choices` already
    admitted one; the per-field `__new__` overloads did not, so the supported
    spelling was rejected at the only place it is ever written.
    """
    results = run_pyright(
        """\
from django.db import models

def flag_choices() -> list[tuple[str, str]]:
    return [("a", "A")]

class Foo(models.Model):
    flag = models.CharField(max_length=64, choices=flag_choices)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_non_interactive_questioner_verbosity_and_log() -> None:
    """A migration-graph check drives the autodetector and wants its reasons.

    NonInteractiveMigrationQuestioner takes `verbosity` and `log` so a caller can
    route the field-level reason somewhere other than stdout. The stub declared
    the subclass as a bare `...`, inheriting a base `__init__` without either.
    """
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
